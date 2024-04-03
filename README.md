# Recursion_MarkdownToHTMLConverter
- マークダウンを HTML に変換するプログラムを作成
- シェルを通して python3 file-converter.py markdown inputfile outputfile というコマンドを実行させる
- markdown は実行するコマンド、inputfile は .md ファイルへのパス、出力パスはプログラムを実行した後に作成される .html
- コマンドライン引数を使用し、変換プロセスを支援する pip を使用してライブラリをインストールおよび管理し、Python の組み込みファイルシステム関数を利用する
- 引数を取得するには、sys.argv を使用
- argv の詳細については Python CLI args リファレンス(https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)を参照
- 引数を解析して、どのようなコマンド（つまり markdown）か、そしてそのコマンドの引数（この場合は入力ファイル文字列と出力文字列）を決定する
- https://python-markdown.github.io/