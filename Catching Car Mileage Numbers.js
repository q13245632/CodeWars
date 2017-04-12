function isInteresting(number, awesomePhrases) {
  var tests = [
    function(n) { return /^\d00+$/.test(n); },
    function(n) { return /^(\d)\1+$/.test(n); },
    function(n) { return RegExp(n).test(1234567890); },
    function(n) { return RegExp(n).test(9876543210); },
    function(n) { return n + '' == (n + '').split('').reverse().join(''); },
    function(n) { return awesomePhrases.some(function(p) { return p == n; }); }
  ];
  
  var interesting = 0;
  tests.some(function(test) {
    if (number > 99 && test(number))
      return interesting = 2;
    else if ((number > 98 && test(number + 1)) || (number > 97 && test(number + 2)))
      interesting = 1;
  });
  return interesting;
}






const chars = n => n.toString().split('')
const match = s => n => new RegExp(n).test(s)
const regex = r => n => r.test(n)

const tests = [
  match('1234567890'),                  // incremental
  match('9876543210'),                  // decremental
  regex(/^\d0+$/),                      // all zeroes
  regex(/^(\d)\1+$/),                   // repeated
  n => n == chars(n).reverse().join('') // palindrome
]

const test = (n, xs) => n > 99 && 
  (xs.indexOf(n) > -1 || tests.map(t => t(n)).some(x => !!x))
  
const isInteresting = (n, xs) =>
  test(n, xs) ? 2 : +(test(n + 1, xs) || test(n + 2, xs))