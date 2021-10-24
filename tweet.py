from datetime import datetime
import config, message
import json
import os
import random
import time
import urllib.parse

import twitterlib

if __name__ == '__main__':
    print('Start at', datetime.now().strftime(config.format_time))

    # init
    api = twitterlib.Twitter(config)
    statuses = {
        '1': '''即戦力！結果を出せる優秀な事業家になろう。

・起業家
・経営者
・個人事業主
・副業, 複業
・フリーランス

コンパスなら、
上記すべてに共通するビジネスのいろはが身に付きます。
https://ogp-generator.hi1280.com/share/kKuTOO3V8rnaERLrH4vM
''',
        '2': '''起業というRPGのルールを学ぼう。

ルールを知らずにゲームに勝つことはできません。

右も左も分からない
起業のルールが学べるのは
スタートアップ･カレッジだけ▼
https://ogp-generator.hi1280.com/share/BY6azup38FvftFHOU0Ap
''',
        '3': '''この内容なのになんで無料でやってるんですか！？

と大好評の0円創業サポート、アクセル。

・起業家
・経営者
・個人事業主
・副業, 複業
・フリーランス

↓詳細、利用者の口コミはこちら。
https://www.notion.so/Accel-f1359237d5b649f7b07acc7629292603'''
    }
    status = random.choice(list(statuses.values()))
    
    # run
    api.tweet(status)

    # done
    print('Finish at', datetime.now().strftime(config.format_time))
