# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .CalcListener import CalcListener
else:
    from CalcListener import CalcListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u";\u015c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\3\2\3\2\5\2M\n\2\3\2\5\2P\n\2\3\2\7\2S\n\2")
        buf.write(u"\f\2\16\2V\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\5\5f\n\5\3\5\3\5\5\5j\n\5\3\5\3\5")
        buf.write(u"\3\6\3\6\7\6p\n\6\f\6\16\6s\13\6\3\6\3\6\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\5\7}\n\7\3\7\3\7\3\7\3\7\5\7\u0083\n\7\3")
        buf.write(u"\b\3\b\3\b\3\b\3\b\3\b\5\b\u008b\n\b\3\t\3\t\3\t\3\t")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\3\f\3\f\5\f\u009f\n\f\3\r\3\r\5\r\u00a3\n\r\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\5\16\u00b6\n\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7")
        buf.write(u"\16\u00c4\n\16\f\16\16\16\u00c7\13\16\3\17\3\17\3\17")
        buf.write(u"\7\17\u00cc\n\17\f\17\16\17\u00cf\13\17\5\17\u00d1\n")
        buf.write(u"\17\3\20\3\20\7\20\u00d5\n\20\f\20\16\20\u00d8\13\20")
        buf.write(u"\3\21\3\21\7\21\u00dc\n\21\f\21\16\21\u00df\13\21\3\22")
        buf.write(u"\3\22\3\22\7\22\u00e4\n\22\f\22\16\22\u00e7\13\22\5\22")
        buf.write(u"\u00e9\n\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write(u"\23\3\24\3\24\3\25\5\25\u00f7\n\25\3\25\3\25\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3")
        buf.write(u"\30\3\30\3\30\5\30\u010a\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\5\33\u011a")
        buf.write(u"\n\33\3\33\3\33\3\33\3\33\5\33\u0120\n\33\3\34\3\34\3")
        buf.write(u"\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u012b\n\34\3\35")
        buf.write(u"\3\35\3\36\3\36\5\36\u0131\n\36\3\37\3\37\3\37\3\37\5")
        buf.write(u"\37\u0137\n\37\3\37\3\37\3 \3 \7 \u013d\n \f \16 \u0140")
        buf.write(u"\13 \3 \3 \3!\3!\3!\3!\5!\u0148\n!\3\"\3\"\5\"\u014c")
        buf.write(u"\n\"\3\"\5\"\u014f\n\"\3#\3#\3#\5#\u0154\n#\3$\3$\3$")
        buf.write(u"\3$\3%\3%\3%\2\3\32&\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2\b\3\2\61\63\3")
        buf.write(u"\2\13\f\3\2\r\16\3\2\17\20\3\2\21\27\3\2\679\u0169\2")
        buf.write(u"J\3\2\2\2\4W\3\2\2\2\6]\3\2\2\2\be\3\2\2\2\nm\3\2\2\2")
        buf.write(u"\f\u0082\3\2\2\2\16\u008a\3\2\2\2\20\u008c\3\2\2\2\22")
        buf.write(u"\u0090\3\2\2\2\24\u0095\3\2\2\2\26\u009e\3\2\2\2\30\u00a2")
        buf.write(u"\3\2\2\2\32\u00b5\3\2\2\2\34\u00d0\3\2\2\2\36\u00d2\3")
        buf.write(u"\2\2\2 \u00d9\3\2\2\2\"\u00e8\3\2\2\2$\u00ee\3\2\2\2")
        buf.write(u"&\u00f3\3\2\2\2(\u00f6\3\2\2\2*\u00fa\3\2\2\2,\u0100")
        buf.write(u"\3\2\2\2.\u0102\3\2\2\2\60\u010b\3\2\2\2\62\u0114\3\2")
        buf.write(u"\2\2\64\u0116\3\2\2\2\66\u0121\3\2\2\28\u012c\3\2\2\2")
        buf.write(u":\u012e\3\2\2\2<\u0132\3\2\2\2>\u013a\3\2\2\2@\u0143")
        buf.write(u"\3\2\2\2B\u0149\3\2\2\2D\u0150\3\2\2\2F\u0155\3\2\2\2")
        buf.write(u"H\u0159\3\2\2\2JL\5\4\3\2KM\5 \21\2LK\3\2\2\2LM\3\2\2")
        buf.write(u"\2MO\3\2\2\2NP\5\36\20\2ON\3\2\2\2OP\3\2\2\2PT\3\2\2")
        buf.write(u"\2QS\5\b\5\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2")
        buf.write(u"U\3\3\2\2\2VT\3\2\2\2WX\7\3\2\2XY\7\64\2\2YZ\7\4\2\2")
        buf.write(u"Z[\5\6\4\2[\\\7\5\2\2\\\5\3\2\2\2]^\7\64\2\2^\7\3\2\2")
        buf.write(u"\2_`\7#\2\2`f\7\64\2\2ab\7$\2\2bc\7\64\2\2cd\7\6\2\2")
        buf.write(u"df\7\7\2\2e_\3\2\2\2ea\3\2\2\2fg\3\2\2\2gi\7\5\2\2hj")
        buf.write(u"\5\36\20\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\5\f\7\2l\t")
        buf.write(u"\3\2\2\2mq\7/\2\2np\5\f\7\2on\3\2\2\2ps\3\2\2\2qo\3\2")
        buf.write(u"\2\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu\7\60\2\2u\13\3\2")
        buf.write(u"\2\2v}\5\20\t\2w}\5\22\n\2x}\5:\36\2y}\5\n\6\2z}\5\66")
        buf.write(u"\34\2{}\58\35\2|v\3\2\2\2|w\3\2\2\2|x\3\2\2\2|y\3\2\2")
        buf.write(u"\2|z\3\2\2\2|{\3\2\2\2}~\3\2\2\2~\177\7\5\2\2\177\u0083")
        buf.write(u"\3\2\2\2\u0080\u0083\5.\30\2\u0081\u0083\5\60\31\2\u0082")
        buf.write(u"|\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write(u"\r\3\2\2\2\u0084\u008b\5\20\t\2\u0085\u008b\5\22\n\2")
        buf.write(u"\u0086\u008b\5:\36\2\u0087\u008b\5\n\6\2\u0088\u008b")
        buf.write(u"\5\66\34\2\u0089\u008b\5.\30\2\u008a\u0084\3\2\2\2\u008a")
        buf.write(u"\u0085\3\2\2\2\u008a\u0086\3\2\2\2\u008a\u0087\3\2\2")
        buf.write(u"\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\17\3")
        buf.write(u"\2\2\2\u008c\u008d\5B\"\2\u008d\u008e\t\2\2\2\u008e\u008f")
        buf.write(u"\5\32\16\2\u008f\21\3\2\2\2\u0090\u0091\7\64\2\2\u0091")
        buf.write(u"\u0092\7\6\2\2\u0092\u0093\5\34\17\2\u0093\u0094\7\7")
        buf.write(u"\2\2\u0094\23\3\2\2\2\u0095\u0096\5B\"\2\u0096\u0097")
        buf.write(u"\7\b\2\2\u0097\u0098\5\26\f\2\u0098\u0099\7\t\2\2\u0099")
        buf.write(u"\u009a\5\30\r\2\u009a\u009b\7\n\2\2\u009b\25\3\2\2\2")
        buf.write(u"\u009c\u009f\7\33\2\2\u009d\u009f\5\32\16\2\u009e\u009c")
        buf.write(u"\3\2\2\2\u009e\u009d\3\2\2\2\u009f\27\3\2\2\2\u00a0\u00a3")
        buf.write(u"\7\33\2\2\u00a1\u00a3\5\32\16\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write(u"\u00a1\3\2\2\2\u00a3\31\3\2\2\2\u00a4\u00a5\b\16\1\2")
        buf.write(u"\u00a5\u00a6\7(\2\2\u00a6\u00b6\5\32\16\t\u00a7\u00b6")
        buf.write(u"\7\33\2\2\u00a8\u00b6\5B\"\2\u00a9\u00b6\5H%\2\u00aa")
        buf.write(u"\u00b6\5\22\n\2\u00ab\u00b6\5\24\13\2\u00ac\u00ad\7\30")
        buf.write(u"\2\2\u00ad\u00ae\7\6\2\2\u00ae\u00af\5\34\17\2\u00af")
        buf.write(u"\u00b0\7\7\2\2\u00b0\u00b6\3\2\2\2\u00b1\u00b2\7\6\2")
        buf.write(u"\2\u00b2\u00b3\5\32\16\2\u00b3\u00b4\7\7\2\2\u00b4\u00b6")
        buf.write(u"\3\2\2\2\u00b5\u00a4\3\2\2\2\u00b5\u00a7\3\2\2\2\u00b5")
        buf.write(u"\u00a8\3\2\2\2\u00b5\u00a9\3\2\2\2\u00b5\u00aa\3\2\2")
        buf.write(u"\2\u00b5\u00ab\3\2\2\2\u00b5\u00ac\3\2\2\2\u00b5\u00b1")
        buf.write(u"\3\2\2\2\u00b6\u00c5\3\2\2\2\u00b7\u00b8\f\16\2\2\u00b8")
        buf.write(u"\u00b9\t\3\2\2\u00b9\u00c4\5\32\16\17\u00ba\u00bb\f\r")
        buf.write(u"\2\2\u00bb\u00bc\t\4\2\2\u00bc\u00c4\5\32\16\16\u00bd")
        buf.write(u"\u00be\f\f\2\2\u00be\u00bf\t\5\2\2\u00bf\u00c4\5\32\16")
        buf.write(u"\r\u00c0\u00c1\f\13\2\2\u00c1\u00c2\t\6\2\2\u00c2\u00c4")
        buf.write(u"\5\32\16\f\u00c3\u00b7\3\2\2\2\u00c3\u00ba\3\2\2\2\u00c3")
        buf.write(u"\u00bd\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c4\u00c7\3\2\2")
        buf.write(u"\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\33\3")
        buf.write(u"\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00cd\5\32\16\2\u00c9")
        buf.write(u"\u00ca\7\31\2\2\u00ca\u00cc\5\32\16\2\u00cb\u00c9\3\2")
        buf.write(u"\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write(u"\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0")
        buf.write(u"\u00c8\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\35\3\2\2\2\u00d2")
        buf.write(u"\u00d6\7\36\2\2\u00d3\u00d5\5\"\22\2\u00d4\u00d3\3\2")
        buf.write(u"\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7")
        buf.write(u"\3\2\2\2\u00d7\37\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00dd")
        buf.write(u"\7\37\2\2\u00da\u00dc\5$\23\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write(u"\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2")
        buf.write(u"\2\u00de!\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e5\5&")
        buf.write(u"\24\2\u00e1\u00e2\7\31\2\2\u00e2\u00e4\5&\24\2\u00e3")
        buf.write(u"\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2")
        buf.write(u"\2\u00e5\u00e6\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5")
        buf.write(u"\3\2\2\2\u00e8\u00e0\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write(u"\u00ea\3\2\2\2\u00ea\u00eb\7\32\2\2\u00eb\u00ec\5(\25")
        buf.write(u"\2\u00ec\u00ed\7\5\2\2\u00ed#\3\2\2\2\u00ee\u00ef\5&")
        buf.write(u"\24\2\u00ef\u00f0\7\25\2\2\u00f0\u00f1\7\33\2\2\u00f1")
        buf.write(u"\u00f2\7\5\2\2\u00f2%\3\2\2\2\u00f3\u00f4\7\64\2\2\u00f4")
        buf.write(u"\'\3\2\2\2\u00f5\u00f7\5*\26\2\u00f6\u00f5\3\2\2\2\u00f6")
        buf.write(u"\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7\64\2")
        buf.write(u"\2\u00f9)\3\2\2\2\u00fa\u00fb\7\34\2\2\u00fb\u00fc\7")
        buf.write(u"\b\2\2\u00fc\u00fd\7\33\2\2\u00fd\u00fe\7\n\2\2\u00fe")
        buf.write(u"\u00ff\7\35\2\2\u00ff+\3\2\2\2\u0100\u0101\5.\30\2\u0101")
        buf.write(u"-\3\2\2\2\u0102\u0103\7 \2\2\u0103\u0104\5\32\16\2\u0104")
        buf.write(u"\u0105\7\"\2\2\u0105\u0109\5\16\b\2\u0106\u010a\7\5\2")
        buf.write(u"\2\u0107\u0108\7!\2\2\u0108\u010a\5\62\32\2\u0109\u0106")
        buf.write(u"\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write(u"/\3\2\2\2\u010b\u010c\7*\2\2\u010c\u010d\7\6\2\2\u010d")
        buf.write(u"\u010e\7\64\2\2\u010e\u010f\7\31\2\2\u010f\u0110\7\64")
        buf.write(u"\2\2\u0110\u0111\7\7\2\2\u0111\u0112\7%\2\2\u0112\u0113")
        buf.write(u"\5\f\7\2\u0113\61\3\2\2\2\u0114\u0115\5\f\7\2\u0115\63")
        buf.write(u"\3\2\2\2\u0116\u0119\7%\2\2\u0117\u0118\7+\2\2\u0118")
        buf.write(u"\u011a\5\32\16\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2")
        buf.write(u"\2\2\u011a\u011b\3\2\2\2\u011b\u011c\5\f\7\2\u011c\u011f")
        buf.write(u"\7,\2\2\u011d\u011e\7+\2\2\u011e\u0120\5\32\16\2\u011f")
        buf.write(u"\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\65\3\2\2\2\u0121")
        buf.write(u"\u0122\7\'\2\2\u0122\u0123\7\64\2\2\u0123\u0124\7\61")
        buf.write(u"\2\2\u0124\u0125\5\32\16\2\u0125\u0126\7&\2\2\u0126\u0127")
        buf.write(u"\5\32\16\2\u0127\u012a\7%\2\2\u0128\u012b\5\n\6\2\u0129")
        buf.write(u"\u012b\5\f\7\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2")
        buf.write(u"\2\u012b\67\3\2\2\2\u012c\u012d\7)\2\2\u012d9\3\2\2\2")
        buf.write(u"\u012e\u0130\7-\2\2\u012f\u0131\5\32\16\2\u0130\u012f")
        buf.write(u"\3\2\2\2\u0130\u0131\3\2\2\2\u0131;\3\2\2\2\u0132\u0133")
        buf.write(u"\5B\"\2\u0133\u0134\5B\"\2\u0134\u0136\5> \2\u0135\u0137")
        buf.write(u"\5\36\20\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write(u"\u0138\3\2\2\2\u0138\u0139\5\n\6\2\u0139=\3\2\2\2\u013a")
        buf.write(u"\u013e\7\6\2\2\u013b\u013d\5@!\2\u013c\u013b\3\2\2\2")
        buf.write(u"\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f")
        buf.write(u"\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141")
        buf.write(u"\u0142\7\7\2\2\u0142?\3\2\2\2\u0143\u0144\5(\25\2\u0144")
        buf.write(u"\u0147\5B\"\2\u0145\u0146\7\61\2\2\u0146\u0148\5\32\16")
        buf.write(u"\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148A\3\2")
        buf.write(u"\2\2\u0149\u014b\7\64\2\2\u014a\u014c\5F$\2\u014b\u014a")
        buf.write(u"\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d")
        buf.write(u"\u014f\5D#\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2")
        buf.write(u"\u014fC\3\2\2\2\u0150\u0151\7\4\2\2\u0151\u0153\7\64")
        buf.write(u"\2\2\u0152\u0154\5F$\2\u0153\u0152\3\2\2\2\u0153\u0154")
        buf.write(u"\3\2\2\2\u0154E\3\2\2\2\u0155\u0156\7\b\2\2\u0156\u0157")
        buf.write(u"\5\32\16\2\u0157\u0158\7\n\2\2\u0158G\3\2\2\2\u0159\u015a")
        buf.write(u"\t\7\2\2\u015aI\3\2\2\2\"LOTeiq|\u0082\u008a\u009e\u00a2")
        buf.write(u"\u00b5\u00c3\u00c5\u00cd\u00d0\u00d6\u00dd\u00e5\u00e8")
        buf.write(u"\u00f6\u0109\u0119\u011f\u012a\u0130\u0136\u013e\u0147")
        buf.write(u"\u014b\u014e\u0153")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'FORM'", u"'.'", u"';'", u"'('", u"')'", 
                     u"'['", u"'..'", u"']'", u"'/'", u"'*'", u"'+'", u"'-'", 
                     u"'and'", u"'or'", u"'>'", u"'<'", u"'<='", u"'>='", 
                     u"'='", u"'<>'", u"'=='", u"'MAX'", u"','", u"':'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"':='", u"'?='", u"'#='" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"LITERAL", u"ARRAY", u"OF", u"VAR", 
                      u"CONSTANT", u"IF", u"ELSE", u"THEN", u"SECTION", 
                      u"PROCEDURE", u"DO", u"TO", u"FOR", u"NOT", u"BREAK", 
                      u"WITHFORMS", u"WHILE", u"LOOP", u"RETURN", u"WS", 
                      u"BEGIN", u"END", u"LET", u"ALTLET", u"CRAZYLET", 
                      u"ID", u"INT", u"STRING", u"TRUE", u"FALSE", u"CHECKED", 
                      u"COMMENT", u"LINE_COMMENT" ]

    RULE_calcfile = 0
    RULE_formset = 1
    RULE_form = 2
    RULE_section = 3
    RULE_block = 4
    RULE_stmt = 5
    RULE_open_stmt = 6
    RULE_assign = 7
    RULE_call = 8
    RULE_multicopy_accum = 9
    RULE_start_index = 10
    RULE_end_index = 11
    RULE_expr = 12
    RULE_argList = 13
    RULE_vardecl = 14
    RULE_constdecl = 15
    RULE_declList = 16
    RULE_constdeclList = 17
    RULE_varDecl = 18
    RULE_r_type = 19
    RULE_arrayDecl = 20
    RULE_ctrlStruct = 21
    RULE_ifStruct = 22
    RULE_withForms = 23
    RULE_elseStruct = 24
    RULE_loopStruct = 25
    RULE_forloopstruct = 26
    RULE_breakStruct = 27
    RULE_ret = 28
    RULE_function = 29
    RULE_formParList = 30
    RULE_formPar = 31
    RULE_full_id = 32
    RULE_sub_id = 33
    RULE_array_index = 34
    RULE_boolean = 35

    ruleNames =  [ u"calcfile", u"formset", u"form", u"section", u"block", 
                   u"stmt", u"open_stmt", u"assign", u"call", u"multicopy_accum", 
                   u"start_index", u"end_index", u"expr", u"argList", u"vardecl", 
                   u"constdecl", u"declList", u"constdeclList", u"varDecl", 
                   u"r_type", u"arrayDecl", u"ctrlStruct", u"ifStruct", 
                   u"withForms", u"elseStruct", u"loopStruct", u"forloopstruct", 
                   u"breakStruct", u"ret", u"function", u"formParList", 
                   u"formPar", u"full_id", u"sub_id", u"array_index", u"boolean" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    LITERAL=25
    ARRAY=26
    OF=27
    VAR=28
    CONSTANT=29
    IF=30
    ELSE=31
    THEN=32
    SECTION=33
    PROCEDURE=34
    DO=35
    TO=36
    FOR=37
    NOT=38
    BREAK=39
    WITHFORMS=40
    WHILE=41
    LOOP=42
    RETURN=43
    WS=44
    BEGIN=45
    END=46
    LET=47
    ALTLET=48
    CRAZYLET=49
    ID=50
    INT=51
    STRING=52
    TRUE=53
    FALSE=54
    CHECKED=55
    COMMENT=56
    LINE_COMMENT=57

    def __init__(self, input):
        super(CalcParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class CalcfileContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.CalcfileContext, self).__init__(parent, invokingState)
            self.parser = parser

        def formset(self):
            return self.getTypedRuleContext(CalcParser.FormsetContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(CalcParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(CalcParser.VardeclContext,0)


        def section(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.SectionContext)
            else:
                return self.getTypedRuleContext(CalcParser.SectionContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_calcfile

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterCalcfile(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitCalcfile(self)




    def calcfile(self):

        localctx = CalcParser.CalcfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calcfile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.formset()
            self.state = 74
            _la = self._input.LA(1)
            if _la==CalcParser.CONSTANT:
                self.state = 73
                self.constdecl()


            self.state = 77
            _la = self._input.LA(1)
            if _la==CalcParser.VAR:
                self.state = 76
                self.vardecl()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.SECTION or _la==CalcParser.PROCEDURE:
                self.state = 79
                self.section()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormsetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.FormsetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def form(self):
            return self.getTypedRuleContext(CalcParser.FormContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_formset

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFormset(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFormset(self)




    def formset(self):

        localctx = CalcParser.FormsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CalcParser.T__0)
            self.state = 86
            self.match(CalcParser.ID)
            self.state = 87
            self.match(CalcParser.T__1)
            self.state = 88
            self.form()
            self.state = 89
            self.match(CalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.FormContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_form

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterForm(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitForm(self)




    def form(self):

        localctx = CalcParser.FormContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_form)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(CalcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SectionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.SectionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def SECTION(self):
            return self.getToken(CalcParser.SECTION, 0)

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def PROCEDURE(self):
            return self.getToken(CalcParser.PROCEDURE, 0)

        def vardecl(self):
            return self.getTypedRuleContext(CalcParser.VardeclContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_section

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterSection(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitSection(self)




    def section(self):

        localctx = CalcParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            token = self._input.LA(1)
            if token in [CalcParser.SECTION]:
                self.state = 93
                self.match(CalcParser.SECTION)
                self.state = 94
                self.match(CalcParser.ID)

            elif token in [CalcParser.PROCEDURE]:
                self.state = 95
                self.match(CalcParser.PROCEDURE)
                self.state = 96
                self.match(CalcParser.ID)
                self.state = 97
                self.match(CalcParser.T__3)
                self.state = 98
                self.match(CalcParser.T__4)

            else:
                raise NoViableAltException(self)

            self.state = 101
            self.match(CalcParser.T__2)
            self.state = 103
            _la = self._input.LA(1)
            if _la==CalcParser.VAR:
                self.state = 102
                self.vardecl()


            self.state = 105
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(CalcParser.BEGIN, 0)

        def END(self):
            return self.getToken(CalcParser.END, 0)

        def stmt(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.StmtContext)
            else:
                return self.getTypedRuleContext(CalcParser.StmtContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_block

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterBlock(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitBlock(self)




    def block(self):

        localctx = CalcParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CalcParser.BEGIN)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.IF) | (1 << CalcParser.FOR) | (1 << CalcParser.BREAK) | (1 << CalcParser.WITHFORMS) | (1 << CalcParser.RETURN) | (1 << CalcParser.BEGIN) | (1 << CalcParser.ID))) != 0):
                self.state = 108
                self.stmt()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(CalcParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.StmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(CalcParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(CalcParser.CallContext,0)


        def ret(self):
            return self.getTypedRuleContext(CalcParser.RetContext,0)


        def block(self):
            return self.getTypedRuleContext(CalcParser.BlockContext,0)


        def forloopstruct(self):
            return self.getTypedRuleContext(CalcParser.ForloopstructContext,0)


        def breakStruct(self):
            return self.getTypedRuleContext(CalcParser.BreakStructContext,0)


        def ifStruct(self):
            return self.getTypedRuleContext(CalcParser.IfStructContext,0)


        def withForms(self):
            return self.getTypedRuleContext(CalcParser.WithFormsContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_stmt

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterStmt(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = CalcParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 128
            token = self._input.LA(1)
            if token in [CalcParser.FOR, CalcParser.BREAK, CalcParser.RETURN, CalcParser.BEGIN, CalcParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 116
                    self.assign()
                    pass

                elif la_ == 2:
                    self.state = 117
                    self.call()
                    pass

                elif la_ == 3:
                    self.state = 118
                    self.ret()
                    pass

                elif la_ == 4:
                    self.state = 119
                    self.block()
                    pass

                elif la_ == 5:
                    self.state = 120
                    self.forloopstruct()
                    pass

                elif la_ == 6:
                    self.state = 121
                    self.breakStruct()
                    pass


                self.state = 124
                self.match(CalcParser.T__2)

            elif token in [CalcParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.ifStruct()

            elif token in [CalcParser.WITHFORMS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.withForms()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Open_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Open_stmtContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(CalcParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(CalcParser.CallContext,0)


        def ret(self):
            return self.getTypedRuleContext(CalcParser.RetContext,0)


        def block(self):
            return self.getTypedRuleContext(CalcParser.BlockContext,0)


        def forloopstruct(self):
            return self.getTypedRuleContext(CalcParser.ForloopstructContext,0)


        def ifStruct(self):
            return self.getTypedRuleContext(CalcParser.IfStructContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_open_stmt

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterOpen_stmt(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitOpen_stmt(self)




    def open_stmt(self):

        localctx = CalcParser.Open_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_open_stmt)
        try:
            self.state = 136
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.ret()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.forloopstruct()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.ifStruct()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.AssignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def full_id(self):
            return self.getTypedRuleContext(CalcParser.Full_idContext,0)


        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def LET(self):
            return self.getToken(CalcParser.LET, 0)

        def ALTLET(self):
            return self.getToken(CalcParser.ALTLET, 0)

        def CRAZYLET(self):
            return self.getToken(CalcParser.CRAZYLET, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_assign

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterAssign(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitAssign(self)




    def assign(self):

        localctx = CalcParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.full_id()
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.LET) | (1 << CalcParser.ALTLET) | (1 << CalcParser.CRAZYLET))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 140
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.CallContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def argList(self):
            return self.getTypedRuleContext(CalcParser.ArgListContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_call

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterCall(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitCall(self)




    def call(self):

        localctx = CalcParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(CalcParser.ID)
            self.state = 143
            self.match(CalcParser.T__3)
            self.state = 144
            self.argList()
            self.state = 145
            self.match(CalcParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multicopy_accumContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Multicopy_accumContext, self).__init__(parent, invokingState)
            self.parser = parser

        def full_id(self):
            return self.getTypedRuleContext(CalcParser.Full_idContext,0)


        def start_index(self):
            return self.getTypedRuleContext(CalcParser.Start_indexContext,0)


        def end_index(self):
            return self.getTypedRuleContext(CalcParser.End_indexContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_multicopy_accum

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterMulticopy_accum(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitMulticopy_accum(self)




    def multicopy_accum(self):

        localctx = CalcParser.Multicopy_accumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multicopy_accum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.full_id()
            self.state = 148
            self.match(CalcParser.T__5)
            self.state = 149
            self.start_index()
            self.state = 150
            self.match(CalcParser.T__6)
            self.state = 151
            self.end_index()
            self.state = 152
            self.match(CalcParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Start_indexContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Start_indexContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(CalcParser.LITERAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_start_index

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterStart_index(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitStart_index(self)




    def start_index(self):

        localctx = CalcParser.Start_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_start_index)
        try:
            self.state = 156
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(CalcParser.LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class End_indexContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.End_indexContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(CalcParser.LITERAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_end_index

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterEnd_index(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitEnd_index(self)




    def end_index(self):

        localctx = CalcParser.End_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_end_index)
        try:
            self.state = 160
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(CalcParser.LITERAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(CalcParser.ExprContext, self).copyFrom(ctx)


    class LogicContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.LogicContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterLogic(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitLogic(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterParens(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitParens(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.BoolContext, self).__init__(parser)
            self.copyFrom(ctx)

        def boolean(self):
            return self.getTypedRuleContext(CalcParser.BooleanContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterBool(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitBool(self)


    class LiteralContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.LiteralContext, self).__init__(parser)
            self.copyFrom(ctx)

        def LITERAL(self):
            return self.getToken(CalcParser.LITERAL, 0)

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitLiteral(self)


    class DivMulContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.DivMulContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterDivMul(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitDivMul(self)


    class MultiCopyAccumulateContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.MultiCopyAccumulateContext, self).__init__(parser)
            self.copyFrom(ctx)

        def multicopy_accum(self):
            return self.getTypedRuleContext(CalcParser.Multicopy_accumContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterMultiCopyAccumulate(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitMultiCopyAccumulate(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.AddSubContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterAddSub(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitAddSub(self)


    class PredicateContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.PredicateContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterPredicate(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitPredicate(self)


    class MaxContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.MaxContext, self).__init__(parser)
            self.copyFrom(ctx)

        def argList(self):
            return self.getTypedRuleContext(CalcParser.ArgListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterMax(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitMax(self)


    class VarRefContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.VarRefContext, self).__init__(parser)
            self.copyFrom(ctx)

        def full_id(self):
            return self.getTypedRuleContext(CalcParser.Full_idContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterVarRef(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitVarRef(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.FunctionCallContext, self).__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(CalcParser.CallContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFunctionCall(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx): # actually a CalcParser.ExprContext)
            super(CalcParser.NotContext, self).__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(CalcParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterNot(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitNot(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = CalcParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 163
                self.match(CalcParser.NOT)
                self.state = 164
                self.expr(7)
                pass

            elif la_ == 2:
                localctx = CalcParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 165
                self.match(CalcParser.LITERAL)
                pass

            elif la_ == 3:
                localctx = CalcParser.VarRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 166
                self.full_id()
                pass

            elif la_ == 4:
                localctx = CalcParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 167
                self.boolean()
                pass

            elif la_ == 5:
                localctx = CalcParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.call()
                pass

            elif la_ == 6:
                localctx = CalcParser.MultiCopyAccumulateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.multicopy_accum()
                pass

            elif la_ == 7:
                localctx = CalcParser.MaxContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.match(CalcParser.T__21)
                self.state = 171
                self.match(CalcParser.T__3)
                self.state = 172
                self.argList()
                self.state = 173
                self.match(CalcParser.T__4)
                pass

            elif la_ == 8:
                localctx = CalcParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(CalcParser.T__3)
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(CalcParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.DivMulContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 182
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.T__8 or _la==CalcParser.T__9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 183
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.AddSubContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 185
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.T__10 or _la==CalcParser.T__11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 186
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = CalcParser.LogicContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 188
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.T__12 or _la==CalcParser.T__13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 189
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = CalcParser.PredicateContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 191
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.T__14) | (1 << CalcParser.T__15) | (1 << CalcParser.T__16) | (1 << CalcParser.T__17) | (1 << CalcParser.T__18) | (1 << CalcParser.T__19) | (1 << CalcParser.T__20))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 192
                        self.expr(10)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ArgListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_argList

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterArgList(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitArgList(self)




    def argList(self):

        localctx = CalcParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.T__3) | (1 << CalcParser.T__21) | (1 << CalcParser.LITERAL) | (1 << CalcParser.NOT) | (1 << CalcParser.ID) | (1 << CalcParser.TRUE) | (1 << CalcParser.FALSE) | (1 << CalcParser.CHECKED))) != 0):
                self.state = 198
                self.expr(0)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CalcParser.T__22:
                    self.state = 199
                    self.match(CalcParser.T__22)
                    self.state = 200
                    self.expr(0)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.VardeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def declList(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.DeclListContext)
            else:
                return self.getTypedRuleContext(CalcParser.DeclListContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_vardecl

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterVardecl(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = CalcParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CalcParser.VAR)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 209
                    self.declList() 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstdeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ConstdeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(CalcParser.CONSTANT, 0)

        def constdeclList(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ConstdeclListContext)
            else:
                return self.getTypedRuleContext(CalcParser.ConstdeclListContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_constdecl

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterConstdecl(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitConstdecl(self)




    def constdecl(self):

        localctx = CalcParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(CalcParser.CONSTANT)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.ID:
                self.state = 216
                self.constdeclList()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.DeclListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def r_type(self):
            return self.getTypedRuleContext(CalcParser.R_typeContext,0)


        def varDecl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(CalcParser.VarDeclContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_declList

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterDeclList(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitDeclList(self)




    def declList(self):

        localctx = CalcParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if _la==CalcParser.ID:
                self.state = 222
                self.varDecl()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CalcParser.T__22:
                    self.state = 223
                    self.match(CalcParser.T__22)
                    self.state = 224
                    self.varDecl()
                    self.state = 229
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 232
            self.match(CalcParser.T__23)
            self.state = 233
            self.r_type()
            self.state = 234
            self.match(CalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstdeclListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ConstdeclListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(CalcParser.VarDeclContext,0)


        def LITERAL(self):
            return self.getToken(CalcParser.LITERAL, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_constdeclList

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterConstdeclList(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitConstdeclList(self)




    def constdeclList(self):

        localctx = CalcParser.ConstdeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constdeclList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.varDecl()
            self.state = 237
            self.match(CalcParser.T__18)
            self.state = 238
            self.match(CalcParser.LITERAL)
            self.state = 239
            self.match(CalcParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.VarDeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_varDecl

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterVarDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = CalcParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(CalcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class R_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.R_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def arrayDecl(self):
            return self.getTypedRuleContext(CalcParser.ArrayDeclContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_r_type

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterR_type(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitR_type(self)




    def r_type(self):

        localctx = CalcParser.R_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_r_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            _la = self._input.LA(1)
            if _la==CalcParser.ARRAY:
                self.state = 243
                self.arrayDecl()


            self.state = 246
            self.match(CalcParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayDeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ArrayDeclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(CalcParser.ARRAY, 0)

        def LITERAL(self):
            return self.getToken(CalcParser.LITERAL, 0)

        def OF(self):
            return self.getToken(CalcParser.OF, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_arrayDecl

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterArrayDecl(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitArrayDecl(self)




    def arrayDecl(self):

        localctx = CalcParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(CalcParser.ARRAY)
            self.state = 249
            self.match(CalcParser.T__5)
            self.state = 250
            self.match(CalcParser.LITERAL)
            self.state = 251
            self.match(CalcParser.T__7)
            self.state = 252
            self.match(CalcParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CtrlStructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.CtrlStructContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ifStruct(self):
            return self.getTypedRuleContext(CalcParser.IfStructContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_ctrlStruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterCtrlStruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitCtrlStruct(self)




    def ctrlStruct(self):

        localctx = CalcParser.CtrlStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ctrlStruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.ifStruct()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.IfStructContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CalcParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def THEN(self):
            return self.getToken(CalcParser.THEN, 0)

        def open_stmt(self):
            return self.getTypedRuleContext(CalcParser.Open_stmtContext,0)


        def ELSE(self):
            return self.getToken(CalcParser.ELSE, 0)

        def elseStruct(self):
            return self.getTypedRuleContext(CalcParser.ElseStructContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_ifStruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterIfStruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitIfStruct(self)




    def ifStruct(self):

        localctx = CalcParser.IfStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifStruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(CalcParser.IF)
            self.state = 257
            self.expr(0)
            self.state = 258
            self.match(CalcParser.THEN)
            self.state = 259
            self.open_stmt()
            self.state = 263
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 260
                self.match(CalcParser.T__2)

            elif la_ == 2:
                self.state = 261
                self.match(CalcParser.ELSE)
                self.state = 262
                self.elseStruct()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithFormsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.WithFormsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WITHFORMS(self):
            return self.getToken(CalcParser.WITHFORMS, 0)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(CalcParser.ID)
            else:
                return self.getToken(CalcParser.ID, i)

        def DO(self):
            return self.getToken(CalcParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_withForms

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterWithForms(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitWithForms(self)




    def withForms(self):

        localctx = CalcParser.WithFormsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_withForms)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(CalcParser.WITHFORMS)
            self.state = 266
            self.match(CalcParser.T__3)
            self.state = 267
            self.match(CalcParser.ID)
            self.state = 268
            self.match(CalcParser.T__22)
            self.state = 269
            self.match(CalcParser.ID)
            self.state = 270
            self.match(CalcParser.T__4)
            self.state = 271
            self.match(CalcParser.DO)
            self.state = 272
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElseStructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ElseStructContext, self).__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_elseStruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterElseStruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitElseStruct(self)




    def elseStruct(self):

        localctx = CalcParser.ElseStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseStruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoopStructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.LoopStructContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.preCond = None # ExprContext
            self.postCond = None # ExprContext

        def DO(self):
            return self.getToken(CalcParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def LOOP(self):
            return self.getToken(CalcParser.LOOP, 0)

        def WHILE(self, i=None):
            if i is None:
                return self.getTokens(CalcParser.WHILE)
            else:
                return self.getToken(CalcParser.WHILE, i)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_loopStruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterLoopStruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitLoopStruct(self)




    def loopStruct(self):

        localctx = CalcParser.LoopStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_loopStruct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(CalcParser.DO)
            self.state = 279
            _la = self._input.LA(1)
            if _la==CalcParser.WHILE:
                self.state = 277
                self.match(CalcParser.WHILE)
                self.state = 278
                localctx.preCond = self.expr(0)


            self.state = 281
            self.stmt()
            self.state = 282
            self.match(CalcParser.LOOP)
            self.state = 285
            _la = self._input.LA(1)
            if _la==CalcParser.WHILE:
                self.state = 283
                self.match(CalcParser.WHILE)
                self.state = 284
                localctx.postCond = self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForloopstructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.ForloopstructContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CalcParser.FOR, 0)

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def TO(self):
            return self.getToken(CalcParser.TO, 0)

        def DO(self):
            return self.getToken(CalcParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(CalcParser.BlockContext,0)


        def stmt(self):
            return self.getTypedRuleContext(CalcParser.StmtContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_forloopstruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterForloopstruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitForloopstruct(self)




    def forloopstruct(self):

        localctx = CalcParser.ForloopstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forloopstruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(CalcParser.FOR)
            self.state = 288
            self.match(CalcParser.ID)
            self.state = 289
            self.match(CalcParser.LET)
            self.state = 290
            self.expr(0)
            self.state = 291
            self.match(CalcParser.TO)
            self.state = 292
            self.expr(0)
            self.state = 293
            self.match(CalcParser.DO)
            self.state = 296
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 294
                self.block()
                pass

            elif la_ == 2:
                self.state = 295
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BreakStructContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.BreakStructContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CalcParser.BREAK, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_breakStruct

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterBreakStruct(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitBreakStruct(self)




    def breakStruct(self):

        localctx = CalcParser.BreakStructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_breakStruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(CalcParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.RetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CalcParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_ret

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterRet(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitRet(self)




    def ret(self):

        localctx = CalcParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(CalcParser.RETURN)
            self.state = 302
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 301
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.FunctionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.retType = None # Full_idContext
            self.fnName = None # Full_idContext

        def formParList(self):
            return self.getTypedRuleContext(CalcParser.FormParListContext,0)


        def block(self):
            return self.getTypedRuleContext(CalcParser.BlockContext,0)


        def full_id(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.Full_idContext)
            else:
                return self.getTypedRuleContext(CalcParser.Full_idContext,i)


        def vardecl(self):
            return self.getTypedRuleContext(CalcParser.VardeclContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_function

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFunction(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFunction(self)




    def function(self):

        localctx = CalcParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            localctx.retType = self.full_id()
            self.state = 305
            localctx.fnName = self.full_id()
            self.state = 306
            self.formParList()
            self.state = 308
            _la = self._input.LA(1)
            if _la==CalcParser.VAR:
                self.state = 307
                self.vardecl()


            self.state = 310
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormParListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.FormParListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def formPar(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.FormParContext)
            else:
                return self.getTypedRuleContext(CalcParser.FormParContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_formParList

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFormParList(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFormParList(self)




    def formParList(self):

        localctx = CalcParser.FormParListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_formParList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(CalcParser.T__3)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.ARRAY or _la==CalcParser.ID:
                self.state = 313
                self.formPar()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self.match(CalcParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormParContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.FormParContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Full_idContext
            self.defaultVal = None # ExprContext

        def r_type(self):
            return self.getTypedRuleContext(CalcParser.R_typeContext,0)


        def full_id(self):
            return self.getTypedRuleContext(CalcParser.Full_idContext,0)


        def LET(self):
            return self.getToken(CalcParser.LET, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_formPar

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFormPar(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFormPar(self)




    def formPar(self):

        localctx = CalcParser.FormParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_formPar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.r_type()
            self.state = 322
            localctx.name = self.full_id()
            self.state = 325
            _la = self._input.LA(1)
            if _la==CalcParser.LET:
                self.state = 323
                self.match(CalcParser.LET)
                self.state = 324
                localctx.defaultVal = self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Full_idContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Full_idContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def array_index(self):
            return self.getTypedRuleContext(CalcParser.Array_indexContext,0)


        def sub_id(self):
            return self.getTypedRuleContext(CalcParser.Sub_idContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_full_id

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterFull_id(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitFull_id(self)




    def full_id(self):

        localctx = CalcParser.Full_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_full_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(CalcParser.ID)
            self.state = 329
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 328
                self.array_index()


            self.state = 332
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 331
                self.sub_id()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sub_idContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Sub_idContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalcParser.ID, 0)

        def array_index(self):
            return self.getTypedRuleContext(CalcParser.Array_indexContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_sub_id

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterSub_id(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitSub_id(self)




    def sub_id(self):

        localctx = CalcParser.Sub_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_sub_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(CalcParser.T__1)
            self.state = 335
            self.match(CalcParser.ID)
            self.state = 337
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 336
                self.array_index()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_indexContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.Array_indexContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CalcParser.RULE_array_index

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterArray_index(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitArray_index(self)




    def array_index(self):

        localctx = CalcParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(CalcParser.T__5)
            self.state = 340
            self.expr(0)
            self.state = 341
            self.match(CalcParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CalcParser.BooleanContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CalcParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CalcParser.FALSE, 0)

        def CHECKED(self):
            return self.getToken(CalcParser.CHECKED, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_boolean

        def enterRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.enterBoolean(self)

        def exitRule(self, listener):
            if isinstance( listener, CalcListener ):
                listener.exitBoolean(self)




    def boolean(self):

        localctx = CalcParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.TRUE) | (1 << CalcParser.FALSE) | (1 << CalcParser.CHECKED))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         



