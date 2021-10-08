# project_name

[![Python 3.9](https://github.com/dbgroup-nagoya-u/template-python/actions/workflows/push.yaml/badge.svg)](https://github.com/dbgroup-nagoya-u/template-python/actions/workflows/push.yaml)

## 概要

## 必要条件

### pyenv/pipenvの準備

[pyenv](https://github.com/pyenv/pyenv-installer)及び[pipenv](https://pipenv-ja.readthedocs.io/ja/translate-ja/install.html#pragmatic-installation-of-pipenv)が使用可能であることを前提とする．
なお，pyenvのインストール時には[前提となるパッケージのインストール](https://github.com/pyenv/pyenv/wiki/Common-build-problems)を忘れないこと．

<!-- 
### 依存ライブラリの準備

依存パッケージで必要なライブラリなどがあればそのインストール方法を書く．
例えば下記のような`apt`経由でのインストール方法など．

```bash
sudo apt install <required_libs>
```
-->

### 開発環境の準備

注：**実行のみを目的とする場合は不要**．

開発に関しては[Visual Studio Code](https://code.visualstudio.com/)の使用を想定する．
また，以下の拡張を使用する．

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)

## 開発/実行手順（Git経由）

開発ないし実行を目的としてインストールする際の手順．
以下，このリポジトリをcloneしたディレクトリに移動済みと想定．

### 開発/実行環境の構築

仮想環境がワーキングディレクトリに生成されるよう`PIPENV_VENV_IN_PROJECT`を設定．

```bash
export PIPENV_VENV_IN_PROJECT=1
```

`pipenv`を用いて開発環境を構築する．

```bash
pipenv sync -d
```

なお，実行のみを目的とする場合は`-d`オプションは不要．

```bash
pipenv sync
```

<!-- 
### その他の準備

その他，特別な準備（環境変数の設定など）が必要な場合はそれを記述．
-->

### 開発

諸々の設定をworkspace settingsとしてリポジトリに含んでいるため，cloneしたディレクトリをVS Codeで開けば，Pythonのpathの解決からテストの検出まで全て自動で行われる．

GitHub Actions用の設定もリポジトリに含んでいるため，`master`ブランチへのpushないしpull requestを行うたびに以下の処理がCIとして回る．

- [black](https://github.com/psf/black)によるコードの整形及び[flake8](https://flake8.pycqa.org/en/latest/)によるコードチェック．
- `tests`ディレクトリ以下に配置された単体テストの実行．

なお，コード整形及びチェックはローカルでもファイル保存時に実行される．

### 実行

コマンドラインからプログラムを起動したい場合，ワーキングディレクトリで下記のように実行する．

```bash
python -m project_name
```

## パッケージとしての利用（pipenv+GitHub経由）

`setup.py`を（最低限だが）記述してあるため，作成したパッケージを`pipenv`（厳密には`pip`）経由でインストールすることも可能．
他のプロジェクトでこのパッケージを使用したい場合はこちらの手順を用いる．

インストールは，下記のように[GitHubのリポジトリ名を指定する](https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#a-note-about-vcs-dependencies)ことで行える．

```bash
pipenv install -e git+ssh://git@github.com/dbgroup-nagoya-u/repository_name.git#egg=project_name
```

インストール後は，その他一般的なパッケージと同様に使用できる．

```python
from project_name import <your_awesome_module>
```

<!--
### 使用例

以下，パッケージとしての使用方法を記述する．
-->
