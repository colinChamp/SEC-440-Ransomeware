# SEC-440-Ransomware

## Powershell preloader 
- Ensures python is installed
- executes python script
- propogates to new machine

## Python script
- encrypts machine
- displays encrypt message

## Psuedo Code
### Powershell Preloader
- Install python and any third party libraries
- Clone python code
- Execute ransomware python code
### Python Main
- Generate symmetric key
- Save key encrypted with an asymmetric key on victim system 
- Load files to be encrypted, C:\Users\*
- Encrypt files and save as copy
- Delete original files
- Clear encryption key from memory
