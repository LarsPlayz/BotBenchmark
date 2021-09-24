// Human Benchmarking - Verbal Memory Test cheat
// Written by Fredrik A. Madsen-Malmo
//
// For educational purposes only. Duh

// Error when trying to access jQuery outside the top-level scope
var words = [];
var j = $;
var last;

function cheat () {
    var word = j('span[ng-bind="word"]').innerHTML;
    last = word;

    if (words.indexOf(word) == -1) {
        words.push(word);
        j('a[ng-click="test.onAnswer(false)"]').click();
    } else {
        j('a[ng-click="test.onAnswer(true)"]').click();
    }
}

interval = setInterval(cheat, 20);
