# 必要なライブラリをインポートします。
import sys
import markdown
from pathlib import Path

def convert_markdown_to_html(input_file, output_file):
    """
    MarkdownファイルをHTMLに変換する関数です。
    
    引数:
    input_file -- 読み込むMarkdownファイルのパス
    output_file -- 生成されるHTMLファイルの保存先のパス
    """

    # 入力ファイルを読み込みます。
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # MarkdownテキストをHTMLに変換します（'tables' 拡張機能を有効に）。
    html = markdown.markdown(text, extensions=['tables'])

    
    # 変換されたHTMLを出力ファイルに書き込みます。
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    """
    メイン関数です。コマンドライン引数を解析して処理を実行します。
    """
    
    # コマンドライン引数を解析します。sys.argv[0]はスクリプト名です。
    if len(sys.argv) == 4 and sys.argv[1].lower() == 'markdown':
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        
        # 入力ファイルが存在することを確認します。
        if not Path(input_file).is_file():
            print(f"エラー: 入力ファイル'{input_file}'が見つかりません。")
            sys.exit(1)
        
        # MarkdownをHTMLに変換します。
        convert_markdown_to_html(input_file, output_file)
        print(f"'{input_file}'を'{output_file}'に変換しました。")
    else:
        print("使用法: python3 MarkdownToHtmlConverter.py markdown inputfile.md outputfile.html")
        sys.exit(1)

if __name__ == "__main__":
    main()
