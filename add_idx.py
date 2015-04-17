# -*- coding:cp932 -*-
import re, sys, codecs

# re._MAXCACHE = 200

wordTbl = {
	u"Cramer-Shoup暗号":u"Cramer-Shoupあんごう",
	u"ElGamal暗号":u"ElGamalあんごう",
	u"RSA暗号":u"RSAあんごう",
	u"RSA-OAEP":u"RSA-OAEP",
	u"危殆化":u"きたいか",
	u"Weierstrassの方程式":u"Weierstrassのほうていしき",
	u"ペー関数":u"ぺーかんすう",
	u"CBCモード":u"CBCもーど",
	u"CTRモード":u"CTRモード",
	u"GCM":u"GCM",
	u"POODLE":u"POODLE",
	u"SSL":u"SSL",
	u"TLS":u"TLS",
	u"LSSS":u"LSSS",
	u"AEAD":u"AEAD",
	u"フィンガープリント":u"ふぃんがーぷりんと",

	u"CRYPTREC":u"CRYPTREC",
	u"NSA":u"NSA",
	u"因子":u"いんし",
	u"正規化":u"せいきか",
	u"Millerのアルゴリズム":u"Millerのあるごりずむ",

	u"DH問題":u"DHもんだい",
	u"DLIN仮定":u"DLINかてい",
	u"BDH問題":u"BDHもんだい",
	u"CDH問題":u"CDHもんだい",
	u"DDH問題":u"DDHもんだい",
	u"SDH問題":u"SDHもんだい",
	u"BDHE問題":u"BDHEもんだい",
	u"BDHI問題":u"BDHIもんだい",
	u"CBDH問題":u"CBDHもんだい",
	u"DBDH問題":u"DBDHもんだい",
	u"IND-CCA2":u"IND-CCA2",

	u"FE":u"FE",
	u"SHE":u"SHE",
	u"LWE":u"LWE",
	u"畳み込み":u"たたみこみ",
	u"対称ペアリング":u"たいしょうぺありんぐ",
	u"非対称ペアリング":u"ひたいしょうぺありんぐ",
	u"双線形写像":u"そうせんけいしゃぞう",

	u"DLP":u"DLP",
	u"DSA":u"DSA",
	u"ECDLP":u"ECDLP",
	u"ECDSA":u"ECDSA",
	u"ECDH":u"ECDH",
	u"楕円DH":u"だえんDH",
	u"EdDSA":u"EdDSA",
	u"CPA":u"CPA",
	u"IND-CCA":u"IND-CCA",
	u"選択平文攻撃":u"せんたくひらぶんこうげき",
	u"選択暗号文攻撃":u"せんたくあんごうぶんこうげき",
	u"サイドチャネル攻撃":u"さいどちゃねるこうげき",
	u"強秘匿性":u"きょうひとくせい",
	u"非展性":u"ひてんせい",
	u"識別不可能性":u"しきべつふかのうせい",
	u"MAC":u"MAC",
	u"PKI":u"PKI",
	u"PSI":u"PSI",
	u"PFS":u"PFS",
	u"RSA仮定":u"RSAかてい",
	u"ブラインド署名":u"ぶらいんどしょめい",
	u"FDH":u"FDH",
	u"Vernam暗号":u"Vernamあんごう",
	u"distortion写像":u"distortionしゃぞう",

	u"乱数":u"らんすう",
	u"暗号理論的擬似乱数":u"あんごうりろんてきぎじらんすう",
	u"トーラス":u"とーらす",
	u"可換群":u"かかんぐん",
	u"結合即":u"けつごうそく",
	u"ランダムウォーク関数":u"らんだむうぉーくかんすう",
	u"巡回群":u"じゅんかいぐん",
	u"生成元":u"せいせいげん",
	u"原始元":u"げんしげん",
	u"単位元":u"たんいげん",
	u"中間者攻撃":u"ちゅうかんしゃこうげき",
	u"MITM":u"MITM",
	u"パディングオラクル攻撃":u"ぱでぃんぐおらくるこうげき",
	u"バイナリ法":u"ばいなりほう",
	u"タイムリリース暗号":u"たいむりりーすあんごう",
	u"排他論理和":u"はいたろんりわ",
	u"離散対数問題":u"りさんたいすうもんだい",
	u"秘密分散":u"ひみつぶんさん",
	u"情報理論的安全":u"じょうほうりろんてきあんぜん",
	u"計算量的安全":u"けいさんりょうてきあんぜん",
	u"属性ベース暗号":u"ぞくせいべーすあんごう",
	u"ゼロ知識証明":u"ぜろちしきしょうめい",
	u"代理暗号":u"だいりあんごう",
	u"再暗号化":u"さいあんごうか",
	u"認証付き暗号":u"にんしょうつきあんごう",
	u"PRE":u"PRE",
	u"IDベース暗号":u"IDべーすあんごう",
	u"因子":u"いんし",
	u"極":u"きょく",
	u"零点":u"れいてん",
	u"位数":u"いすう",
	u"結託攻撃":u"けったくこうげき",
	u"拡大体":u"かくだいたい",
	u"素体":u"そたい",
	u"標数":u"ひょうすう",
	u"Euclidの互除法":u"Euclidのごじょほう",
	u"ハッシュ関数":u"はっしゅかんすう",
	u"デジタル署名":u"でじたるしょめい",
	u"伸長攻撃":u"しんちょうこうげき",
	u"原像計算":u"げんぞうけいさん",

	u"ミックスネット":u"みっくすねっと",
	u"再暗号化":u"さいあんごうか",

	u"射影空間":u"しゃえいくうかん",
	u"アフィン":u"あふぃん",
	u"斉次多項式":u"せいじたこうしき",
	u"DPVS":u"DPVS",
	u"attribute-hiding":u"attribute-hiding",
	u"payload-hiding":u"payload-hiding",
	u"private-index":u"private-index",
	u"public-index":u"public-index",
	u"bootstrap":u"bootstrap",
	u"多重線形写像":u"たじゅうせんけいしゃぞう",
	u"内積暗号":u"ないせきあんごう",
	u"関数型暗号":u"かんすうがたあんごう",
	u"述語暗号":u"じゅつごあんごう",
	u"ワンタイムパッド":u"わんたいむぱっど",

	u"Lagrange補間":u"Lagrangeほかん",
#	u"Lagrange係数":u"Lagrangeけいすう",
#	u"Vandermonde行列":u"Vandermondeぎょうれつ",
#	$\rho$法
}

def addIndex(inFile):
	if not inFile.endswith('tex'):
		return
	outFile = '_' + inFile
	fi = codecs.open(inFile, 'r', encoding = 'cp932')
	s = fi.read()
	fi.close()

	for (word, furigana) in wordTbl.items():
		r = u'%s\index{%s@%s}' % (word, furigana, word)
		s = re.sub('([^a-zA-Z])' + word, '\\1' + r, s)
	s = s.replace(u'。', u'．')
	s = s.replace(u'、', u'，')

	fo = codecs.open(outFile, 'w', encoding = 'cp932')
	fo.write(s)
	fo.close()

def main():
	if len(sys.argv) != 2:
		print "usage: add_idx.py input.tex"
	addIndex(sys.argv[1])

if __name__ == '__main__':
	main()
