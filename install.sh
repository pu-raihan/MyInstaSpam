clear
echo "[*] Initiating install......"
pip install selenium
echo "[*] Selenium module installed...."
echo "[*] Setting up drivers......"
sudo chmod +x chromedriver
sudo chmod +x geckodriver
sudo cp chromedriver /usr/bin
sudo cp geckodriver /usr/bin
echo "[*] Drivers setup successful......"
echo "[*] Installation completed successfully."
echo " "
echo "[*] Launching the program...."
python3 myinsta.py
