class Config:
    source = {
        'http://webdown2.nexon.co.jp/arad/real/': {
            'format': 'spk', 'list': 'package.lst'},
        'http://d-fighter.dn.nexoncdn.co.kr/samsungdnf/neople/dnf_hg/': {
            'format': 'spk', 'list': 'package.lst'},
        'http://d-fighter.dn.nexoncdn.co.kr/samsungdnf/neople/dnf_open/': {
            'format': 'spk', 'list': 'package.lst'},
        'http://download.dfoneople.com/Patch/': {
            'format': 'spk', 'list': 'package.lst'},
        'http://down-update.qq.com/dnf/autopatch/dnf_exp/dnf.exp2.full.tct/': {
            'format': 'tct', 'list': 'auto.lst'},
    }

    down_dir = './Download'

    block_size = 1024

    retry_count = 5