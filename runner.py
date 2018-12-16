from GetUtaNet import GetLyr
from LyrAnalyzer import TxtAnalyze

if __name__ == '__main__':
    '''
    GetLyr().main('https://www.uta-net.com/artist/19617/', 'PoppinParty')
    GetLyr().main('https://www.uta-net.com/artist/22197/', 'Roselia')
    GetLyr().main('https://www.uta-net.com/artist/22806/', 'HelloHappyWorld')
    GetLyr().main('https://www.uta-net.com/artist/23083/', 'Afterglow')
    GetLyr().main('https://www.uta-net.com/artist/22674/', 'PastelPalettes')
    '''

    TxtAnalyze().all_words_counter('PoppinParty')
    TxtAnalyze().all_words_counter('Roselia')
    TxtAnalyze().all_words_counter('HelloHappyWorld')
    TxtAnalyze().all_words_counter('Afterglow')
    TxtAnalyze().all_words_counter('PastelPalettes')
