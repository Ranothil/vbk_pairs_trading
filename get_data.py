'''
Created on November 2nd, 2020
Pulls historical price data from yahoo finance for list of vbk constituents
@Zachary Lee
@Xiaoying Tang
'''

from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
import datetime

ls_vbk_constituents = ['IMMU', 'HZNP', 'PODD', 'ETSY', 'CTLT', 'ZBRA', 'TER', 'HUBS', 'POOL', 'FICO', 'MPWR', 'ZEN',
                       'TDY', 'MASI', 'CDAY', 'BIO', 'MDB', 'SRPT', 'GGG', 'ELS', 'PENN', 'NDSN', 'ENTG', 'CABO',
                       'AVTR', 'TECH', 'NVCR', 'LII', 'ZNGA', 'COUP', 'ENPH', 'NBIX', 'BFAM', 'TTC', 'TDOC', 'GWRE',
                       'EPAM', 'AZPN', 'PTC', 'CHGG', 'FIVN', 'CONE', 'LVGO', 'CZR', 'GH', 'TREX', 'GLIBA', 'RGLD',
                       'SAM', 'BYND', 'QDEL', 'PLAN', 'CHE', 'OLED', 'FSLY', 'WSO', 'AMH', 'EXEL', 'DT', 'AMED', 'G',
                       'STE', 'Z', 'AOS', 'FND', 'COLD', 'RGEN', 'COG', 'TYL', 'FIVE', 'IAA', 'CREE', 'FWONK', 'BURL',
                       'GRUB', 'IRTC', 'DNKN', 'PEN', 'CASY', 'TNDM', 'IONS', 'MYOK', 'BERY', 'GNTX', 'PRAH', 'NET',
                       'RUN', 'CUBE', 'MNTA', 'WEX', 'JKHY', 'LHCG', 'STOR', 'CIEN', 'MKSI', 'MANH', 'ESTC', 'PFPT',
                       'KRC', 'IPHI', 'XLRN', 'AYX', 'RH', 'SMAR', 'PCTY', 'REXR', 'HTA', 'AAXN', 'CHDN', 'CRL', 'BLD',
                       'NTRA', 'BWXT', 'SITE', 'ERIE', 'CGNX', 'LITE', 'RP', 'CDK', 'AVLR', 'COR', 'POST', 'ZS', 'SYNH',
                       'OLLI', 'RARE', 'PEGA', 'LSTR', 'ACAD', 'BPMC', 'ACC', 'PLNT', 'EBS', 'FLIR', 'QTWO', 'STAG',
                       'NVRO', 'TW', 'RDFN', 'EVBG', 'HAE', 'EEFT', 'MRCY', 'BL', 'ARNA', 'TPX', 'SLAB', 'MTN', 'IIVI',
                       'SSD', 'ARWR', 'NATI', 'MMS', 'FRPT', 'NTNX', 'CCMP', 'LFUS', 'NEOG', 'WING', 'DLB', 'STMP',
                       'KNSL', 'TXRH', 'BRKR', 'WMGI', 'ENV', 'NXST', 'QTS', 'ADPT', 'SKX', 'LSCC', 'NEO', 'LOPE',
                       'HQY', 'HST', 'EXPO', 'TRNO', 'PSTG', 'DOC', 'GMED', 'VRT', 'BLUE', 'FOLD', 'HALO', 'ICUI',
                       'YETI', 'NOVT', 'Y', 'EXP', 'SMTC', 'SRC', 'BRKS', 'VRNS', 'BAND', 'PRLB', 'MORN', 'FGEN',
                       'FTDR', 'IART', 'INSM', 'QLYS', 'SAIA', 'SAIL', 'GBT', 'HPP', 'CACC', 'ASGN', 'REG', 'MEDP',
                       'POWI', 'BCPC', 'JCOM', 'LPSN', 'CHH', 'OMCL', 'EYE', 'FOXF', 'DECK', 'PTCT', 'NEWR', 'NEU',
                       'NKTR', 'AJRD', 'JBT', 'NFE', 'ROLL', 'PE', 'LAMR', 'ENSG', 'BLKB', 'ACIW', 'RPD', 'MSGS', 'CLH',
                       'FSLR', 'NVTA', 'WMS', 'FATE', 'HRC', 'SPSC', 'AMN', 'FEYE', 'PZZA', 'CROX', 'AZEK', 'COHR',
                       'CWST', 'SPCE', 'ALKS', 'PLUG', 'CCOI', 'WDFC', 'COLM', 'ACIA', 'PSB', 'BOX', 'PNFP', 'TENB',
                       'VSLR', 'GTLS', 'AAON', 'LCII', 'MIDD', 'ALRM', 'DORM', 'NUVA', 'AEIS', 'ORA', 'PCRX', 'VIR',
                       'NSP', 'TREE', 'TNET', 'DOOR', 'TWOU', 'SHAK', 'ALLO', 'BYD', 'HHC', 'KWR', 'ALLK', 'FELE', 'FN',
                       'WWD', 'ITRI', 'DIOD', 'STRA', 'MMSI', 'CLDR', 'VIRT', 'IBP', 'XNCR', 'ADSW', 'GKOS', 'ONEM',
                       'CSOD', 'AGIO', 'ZG', 'EXLS', 'SHEN', 'HMSY', 'DEI', 'SILK', 'IRBT', 'APPF', 'NGVT', 'HR',
                       'SGMS', 'AQUA', 'WPX', 'DCPH', 'ESNT', 'FORM', 'BMI', 'PPBI', 'INOV', 'WWE', 'SMPL', 'CUB',
                       'ROG', 'JJSF', 'NSA', 'CORT', 'CARG', 'CVLT', 'EDIT', 'RHP', 'EPAY', 'SWAV', 'IDCC', 'HLNE',
                       'PS', 'JBGS', 'AMBA', 'LANC', 'VRM', 'FIT', 'CTRE', 'JACK', 'AWI', 'ALTR', 'SIX', 'DY', 'MWA',
                       'INSP', 'VSAT', 'FWRD', 'MTSI', 'IBTX', 'CMD', 'VICR', 'AL', 'AIMT', 'SFBS', 'MXL', 'ABCB', 'BE',
                       'HLI', 'HASI', 'LGND', 'SONO', 'YEXT', 'BEAT', 'WAL', 'UPWK', 'IRWD', 'ATSG', 'SBRA', 'YELP',
                       'SFIX', 'CCXI', 'IIPR', 'FOUR', 'AVAV', 'RVMD', 'THRM', 'CNS', 'LTHM', 'MSGE', 'PGRE', 'TWST',
                       'WSC', 'STAA', 'HRTX', 'MNRO', 'SWI', 'EGOV', 'PRO', 'VRRM', 'APPN', 'PDCE', 'LGIH', 'KTOS',
                       'GSHD', 'PD', 'ICPT', 'CMPR', 'LMNX', 'COKE', 'PING', 'PLMR', 'PGNY', 'RRR', 'FCFS', 'CNMD',
                       'CWT', 'FARO', 'MSTR', 'HLIO', 'UI', 'TNC', 'LNN', 'SUPN', 'FOCS', 'SEAS', 'APG', 'NTLA', 'STL',
                       'ZUO', 'EVOP', 'EVH', 'UNIT', 'INFN', 'LPRO', 'EPZM', 'KRG', 'SDC', 'SAFE', 'PNTG', 'CVA',
                       'EHTH', 'MTDR', 'HTLD', 'WHD', 'USNA', 'ITCI', 'HGV', 'FIX', 'KW', 'ELY', 'RGNX', 'MED', 'APLS',
                       'SWCH', 'RWT', 'PSN', 'CEVA', 'TFSL', 'LASR', 'UTZ', 'BRBR', 'PEB', 'BIGC', 'FWONA', 'CHX',
                       'FIZZ', 'RAVN', 'ALGT', 'AIN', 'TBPH', 'NBHC', 'CRVL', 'EB', 'CVCO', 'ANGI', 'RLAY', 'OPCH',
                       'PLAY', 'CASH', 'SHOO', 'BLI', 'OPK', 'UHT', 'GOSS', 'NARI', 'EAF', 'SSP', 'VRTU', 'SLQT', 'MMI',
                       'BEAM', 'SNBR', 'JAMF', 'IMVT', 'INVA', 'CLNY', 'JOE', 'KRNY', 'ALEC', 'FROG', 'AMWD', 'EXPI',
                       'VECO', 'OFIX', 'RXT', 'DDD', 'GOCO', 'SGMO', 'CKH', 'HCAT', 'QUOT', 'INGN', 'ATNI', 'EBIX',
                       'LRN', 'AMWL', 'RDUS', 'HSTM', 'LBRT', 'ALX', 'ESPR', 'ACCD', 'ZNTL', 'CWH', 'DRQ', 'WW', 'ATRA',
                       'RMR', 'RESI', 'RVLV', 'REAL', 'PCVX', 'ELF', 'SCPL', 'FORR', 'EIGI', 'THR', 'AVD', 'MOBL',
                       'GRC', 'IPAR', 'SPPI', 'NEX', 'GSKY', 'BNL', 'NTUS', 'LMND', 'GBIO', 'DCT', 'PTVE', 'AKCA',
                       'ZIOP', 'VERX', 'WOW', 'PTEN', 'PHAT', 'OM', 'GOGO', 'NKTX', 'CLVS', 'RIG', 'PGEN', 'TRUE',
                       'VVNT', 'LORL', 'TCDA', 'VITL', 'ALVR', 'STEP', 'AMK', 'PUMP', 'GSAT', 'OII', 'BNFT', 'SUMO',
                       'KYMR', 'RUBY', 'SCWX', 'GTT', 'REV', 'GBL']

dt_start = datetime.datetime(2013, 1, 1)
dt_end = datetime.datetime(2020, 11, 2)
today = date.today()

files=[]



def getData(ticker):
    print (ticker)
    data = pdr.get_data_yahoo(ticker, start=dt_start, end=dt_end)
    dataname= ticker+"_"+str(today)
    files.append(dataname)
    SaveData(data, dataname)

def SaveData(df, filename):
    df.to_csv("C:\\Users\\q9237\\PycharmProjects\\vbk_pairs_trading\\data"+filename +".csv")

for s_ticker in ls_vbk_constituents:
    getData(s_ticker)

for i in range(0,len(ls_vbk_constituents)):
    df1= pd.read_csv("C:\\Users\\q9237\\PycharmProjects\\vbk_pairs_trading\\data"+ str(files[i])+".csv")
    print (df1.head())



