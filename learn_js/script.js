'use strict';
//задание 1
let number = prompt('Enter number', '');

if (number > 0 ){
    alert(1);
} else if (number < 0){
    alert(-1);
} else {
    alert(0);
}
//задание 2
let result;

if (a + b < 4) {
  result = 'Мало';
} else {
  result = 'Много';
}

result = (a + b < 4) ? 'Мало' : 'Много';
//задание 3
let message;

let meassage = (login = 'сотрудник') ? message = 'Привет' :
    (login = 'директор') ? message = 'здравствуйте' :
    (login = '') ? message = 'Нет логина' : '';

//задание 4
let userName = prompt('введите ваше имя', '');

if (name === 'Админ'){
    let pass = prompt('введите пароль', '');
    if(pass === 'Я главный'){
      alert('Здравствуйте');
    } else if(pass === null || pass === ''){
      alert('Отменено');
    } else {
      alert('Неверный пароль');
    }
} else if(name === null || name === ''){
  alert('Отменено');
} else {
  alert('Я вас не знаю');
}
//задание 5
let num1 = 10,
    num2 = 20;
    // result;

if (result === null || result === undefined) {
  if (num1 !== null && num1 !== undefined) {
    result = num1;
  } else {
    result = num2;
  }
}
result ??= num1 ?? num2;
//задание 6
for (let i = 2; i <=10 ; i++) {
  if (i % 2 == 0) {
    alert(i);
  }
}
//задание 7
for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}

let i = 0;
while (i < 3) {
  alert( `number ${i}!` );
  i++;
}
//задание 8
let num;
do {
  num = prompt('Enter number', '');
} while (num <= 100 && num);

//задание 9
let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) {
  for (let j = 2; j < i; i++){
    if (i % j == 0) continue nextPrime;
  }
  alert(i);
}