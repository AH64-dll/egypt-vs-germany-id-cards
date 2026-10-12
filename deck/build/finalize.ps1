param(
  [Parameter(Mandatory=$true)][string]$In,        # draft pptx from python-pptx
  [Parameter(Mandatory=$true)][string]$Out,       # final pptx (fonts embedded)
  [string]$Pdf = "",
  [string]$PngDir = "",
  [int]$Width = 1920,
  [string]$Only = ""                              # e.g. "1,6,33" to export selected slides only
)
$ErrorActionPreference = "Stop"
$ppt = New-Object -ComObject PowerPoint.Application
try {
  $pres = $ppt.Presentations.Open((Resolve-Path $In).Path, $true, $false, $false)   # ReadOnly, Untitled=false, WithWindow=false
  # 24 = ppSaveAsOpenXMLPresentation ; EmbedTrueTypeFonts = msoTrue (-1)
  $outFull = [System.IO.Path]::GetFullPath($Out)
  $pres.SaveAs($outFull, 24, -1)
  if ($Pdf -ne "") { $pres.SaveAs([System.IO.Path]::GetFullPath($Pdf), 32) }   # 32 = ppSaveAsPDF
  if ($PngDir -ne "") {
    New-Item -ItemType Directory -Force $PngDir | Out-Null
    $h = [int]($Width * 9 / 16)
    $sel = @()
    if ($Only -ne "") { $sel = $Only.Split(",") | ForEach-Object { [int]$_ } }
    foreach ($sl in $pres.Slides) {
      if ($sel.Count -gt 0 -and -not ($sel -contains $sl.SlideIndex)) { continue }
      $f = Join-Path ([System.IO.Path]::GetFullPath($PngDir)) ("s{0:D2}.png" -f $sl.SlideIndex)
      $sl.Export($f, "PNG", $Width, $h)
    }
  }
  # overflow report: text frames whose text is taller than the frame
  $rep = @()
  foreach ($sl in $pres.Slides) {
    foreach ($sh in $sl.Shapes) {
      if ($sh.HasTextFrame -and $sh.TextFrame2.HasText) {
        $bh = $sh.TextFrame2.TextRange.BoundHeight; $bw = $sh.TextFrame2.TextRange.BoundWidth
        if ($bh -gt ($sh.Height + 4) -or $bw -gt ($sh.Width + 6)) {
          $t = $sh.TextFrame2.TextRange.Text; if ($t.Length -gt 40) { $t = $t.Substring(0,40) }
          $rep += ("OVERFLOW s{0:D2} '{1}' frame={2:N0}x{3:N0} text={4:N0}x{5:N0} :: {6}" -f $sl.SlideIndex, $sh.Name, $sh.Width, $sh.Height, $bw, $bh, ($t -replace "`r|`n"," "))
        }
      }
    }
  }
  $pres.Close()
  if ($rep.Count -gt 0) { $rep } else { "NO_OVERFLOW" }
}
finally {
  $ppt.Quit()
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
}
