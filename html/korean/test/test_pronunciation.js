try {
var pronunciation = require('../pronunciation'),
    assert        = require('assert'),
    sys           = require('sys');
} catch(e) {}

assert.deepEqual(pronunciation.move_padchim_to_replace_eung('학', '원'), ['하', '권']);

to_digut = pronunciation.change_padchim_pronunciation('ᆮ', {'ᆺ': true, 'ᆻ': true, 'ᆽ': true, 'ᆾ': true, 'ᇀ': true, 'ᇂ': true});
assert.deepEqual(to_digut('했', ''), ['핻', '']);

giyuk_to_eung = pronunciation.consonant_combination_rule('ᆨ', 'ᄆ', 'ᆼ', 'ᄆ');
assert.deepEqual(giyuk_to_eung('국', '물'), ['궁', '물']);

[['국물',       '궁물'],
 ['격노하다',   '경노하다'],
 ['큌넷',       '큉넫'],
 ['부엌문',     '부엉문'],
 ['닫는',       '단는'],
 ['묻몸',       '문몸'],
 ['덧니',       '던니'],
 ['했나',       '핸나'],
 ['거짓말',     '거진말'],
 ['국수',       '국쑤'],
 ['북한',       '부칸'],
 ['그렇다',     '그러타'],
 ['받이',       '바지'],
 ['같이',       '가치'],
 ['젖니',       '전니'],
 ['낮말',       '난말'],
 ['옻나무',     '온나무'],
 ['옻물',       '온물'],
 ['맡는',       '만는'],
 ['낱말',       '난말'],
 ['놓는',       '논는'],
 ['놓말',       '논말'],
 ['굽는',       '굼는'],
 ['업무',       '엄무'],
 ['엎는',       '엄는'],
 ['그렇게',     '그러케'],
 ['걷하',       '거타'],
 ['급하다',     '그파다'],
 ['낳부',       '나푸'],
 ['맞히다',     '마치다'],
 ['놓지마',     '노치마'],
 ['그렇지',     '그러치'],
 ['역량',       '영냥'],
 ['선릉',       '설릉'],
 ['암루',       '암누'],
 ['강력',       '강녁'],
 ['잡록',       '잠녹'],
 ['앉아',       '안자'],
 ['잃어버리다', '이러버리다'],
 ['앉는',       '안는'],
 ['닮다',       '담다'],
 ['닮아',       '달마'],
 ['못하다',     '모타다'],
 ['학교',       '학꾜'],
 ['손이',       '소니'],
 ['산에',       '사네'],
 ['돈을',       '도늘'],
 ['문으로',     '무느로'],
 ['좋은',       '조은'],
 ['낳다',       '나타'],
 ['옷',         '옫'],
 ['앞',         '압'],
 ['요?',        '요?'],
 ['있습니다',   '이씀니다'],
 ['__요',       '__요'],
 ['있다',       '이따']].forEach(function(test_data) {
     input = test_data[0];
     expected = test_data[1];
     assert.equal(pronunciation.get_pronunciation(input), expected);
});
