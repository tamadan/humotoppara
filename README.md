# humotoppara
ふもとっぱらのキャンセル拾いをするアプリケーション

# プロジェクト概要

このプロジェクトは、特定のキャンプサイトの予約状況を確認し、空きがあれば自動で予約を行うPythonスクリプトです。Seleniumを使用してブラウザ操作を自動化し、指定されたサイトと日付に基づいて予約を試みます。

## 事前準備

1. 予約サイトの会員登録を行ってください。
   - [Fumotoppara予約サイト](https://reserve.fumotoppara.net/)で会員登録を済ませてください。

2. 必要なPythonパッケージをインストールします。
   - `pipenv`を使用してパッケージを管理しています。以下のコマンドでインストールを行ってください。

   ```bash
   pipenv install
   ```

3. `.env`ファイルを作成し、ログイン情報を設定します。

   ```plaintext
   LOGIN_EMAIL=your_email@example.com
   LOGIN_PASSWORD=your_password
   ```

4. **Google Chromeをインストールします。**
   - `chromedriver`を使用しているため、Google Chromeが必要です。お使いのOSに合わせて[Google Chromeの公式サイト](https://www.google.com/chrome/)からインストールしてください。

## 動作手順

1. スクリプトは指定されたキャンプサイトと日付に基づいて予約を試みます。予約枠が空いていなかった場合はキャンセル待ちの為30分ごとに予約を試みます。

   - 予約するサイトと日付は`main.py`ファイル内で指定されています。以下のように指定されています。

   ```python
   getCampStock(content.SITE_GROUP.suizanso, ["2025-01-20", "2025-01-24", "2025-01-26"])
   ```

   - `content.SITE_GROUP.suizanso`は予約するサイトを表し、日付のリストは予約を試みる日付を表します。リストの左側が優先度の高い日付で、先にヒットした日付を取りにいくようになっています。

2. プロジェクトのルートディレクトリで以下のコマンドを実行し、スクリプトを開始します。

   ```bash
   pipenv run main
   ```

3. スクリプトの動作中にブラウザが自動で開き、予約手続きが進行します。予約に必要な情報を記入する時間が20分確保されています。

## 指定可能なキャンプサイト

以下のキャンプサイトを指定することができます。

- キャンプ日帰り (`content.SITE_GROUP.campDay`)
- キャンプ宿泊 (`content.SITE_GROUP.campStay`)
- コテージ柏 (`content.SITE_GROUP.cottageKashiwa`)
- 翠山荘 (`content.SITE_GROUP.suizanso`)
- 毛無山荘 (`content.SITE_GROUP.kenashisan`)
- 金山キャビン (`content.SITE_GROUP.kanayamaCabin`)
- コロッケ (`content.SITE_GROUP.korokke`)

## 注意事項

- スクリプトを実行する前に、必ず`.env`ファイルに正しいログイン情報を設定してください。
- 予約サイトの仕様変更により、スクリプトが正常に動作しない場合があります。その際はコードの修正が必要です。
- **ループ処理に関する注意**: このプログラムは予約が成功するまで30分ごとに予約を試みるループ処理を行います。予約が成功するか、プログラムを手動で停止するまで実行され続けるため注意してください。
