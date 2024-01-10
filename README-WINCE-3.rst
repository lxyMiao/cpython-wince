# Python-for-WinCE(工事中)

Windows CE に移植されたPython3.10.10です。[cpython](https://github.com/python/cpython) 及び [PythonCE(2.5)](https://sourceforge.net/projects/pythonce/) を元に作成されました。

**!!! すべて自己責任で行ってください !!!**
ビルド及び使用に際して発生したいかなる事象についても、RasPythonは一切の責任を負いません。

## ビルド手順
### Linuxの場合:
必要な環境:
- debian系Linux(amd64)
1. gcc-arm-mingw32ceをインストール( https://max.kellermann.name/projects/cegcc/ を参照)
  ```
echo "deb https://max.kellermann.name/debian cegcc_buster-default main" >>  /etc/apt/sources.list
apt-get update
apt-get install gcc-arm-mingw32ce
```
2. このリポジトリをクローンしてビルド
```
git clone https://github.com/RasPython3/Python-for-WinCE.git
cd Python-for-WinCE/
./ce_build.sh && ./ce_pack.sh
```
3. wince_buildにファイル一式が生成されています。
### Windowsの場合:
(未対応)
