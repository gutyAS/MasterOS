Write-Host "[Autoscaler] Start gutyAS MasterOS"
$loop=0
while ($true) {
  $loop++
  Write-Host ("[Autoscaler] Kontrola #{0} v {1}" -f $loop,(Get-Date))
  Start-Sleep -Seconds 600
}
