from datetime import datetime
import config_seitaconsulting, message
import json
import os
import random
import time
import urllib.parse

import twitterlib

if __name__ == '__main__':
    print('Start at', datetime.now().strftime(config_seitaconsulting.format_time))

    # init
    api = twitterlib.Twitter(config_seitaconsulting)
    statuses = {
        '1': '''いつも応援ありがとうございます。有益情報を一人でも多くの起業家に発信し「望めば誰もが起業家として活躍できる社会」を実現したいと考えています。「いいね」や「リプライ」で交流してもらえるとモチベーションが上がります。今後ともよろしくお願いいたします。
'''
    }
    status = random.choice(list(statuses.values()))
    
    # run
    api.tweet(status)

    # done
    print('Finish at', datetime.now().strftime(config_seitaconsulting.format_time))
