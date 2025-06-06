"""
このファイルは、固定の文字列や数値などのデータを変数として一括管理するファイルです。
"""

############################################################
# 共通変数の定義
############################################################

# ==========================================
# 画面表示系
# ==========================================
APP_NAME = "対話型商品レコメンド生成AIアプリ"
USER_ICON_FILE_PATH = "./images/user_icon.jpg"
AI_ICON_FILE_PATH = "./images/ai_icon.jpg"
INFORMATION_ICON = ":material/information:"
WARNING_ICON = ":material/warning:"
ERROR_ICON = ":material/error:"
CHAT_INPUT_HELPER_TEXT = "こちらからお探しの商品の特徴や名前を入力してください。"
SPINNER_TEXT = "レコメンドする商品の検討中..."


# ==========================================
# ログ出力系
# ==========================================
LOG_DIR_PATH = "./logs"
LOGGER_NAME = "ApplicationLog"
LOG_FILE = "application.log"
APP_BOOT_MESSAGE = "アプリが起動されました。"

# ==========================================
# Retriever設定系
# ==========================================
TOP_K = 5
RETRIEVER_WEIGHTS = [0.5, 0.5]


# ==========================================
# RAG参照用のデータソース系
# ==========================================
RAG_SOURCE_PATH = "./data/products.csv"


# ==========================================
# エラー・警告メッセージ
# ==========================================
COMMON_ERROR_MESSAGE = "このエラーが繰り返し発生する場合は、管理者にお問い合わせください。"
INITIALIZE_ERROR_MESSAGE = "初期化処理に失敗しました。"
CONVERSATION_LOG_ERROR_MESSAGE = "過去の会話履歴の表示に失敗しました。"
RECOMMEND_ERROR_MESSAGE = "商品レコメンドに失敗しました。"
LLM_RESPONSE_DISP_ERROR_MESSAGE = "商品情報の表示に失敗しました。"