'use strict';
//задание 1
// let number = prompt('Enter number', '');

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
// let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) {
  for (let j = 2; j < i; i++){
    if (i % j == 0) continue nextPrime;
  }
  alert(i);
}

//задание 10
switch (browser) {
  case 'Edge':
    alert( "You've got the Edge!" );
    break;

  case 'Chrome':
  case 'Firefox':
  case 'Safari':
  case 'Opera':
    alert( 'Okay we support these browsers too' );
    break;

  default:
    alert( 'We hope that this page looks ok!' );
}

if (browser == 'Edge'){
  alert( "You've got the Edge!" );
} else if (browser == 'Chrome'
  || browser == 'Firefox'
  || browser == 'Safari'
  || browser == 'Opera') {
  alert( 'Okay we support these browsers too' );
} else {
  alert( 'We hope that this page looks ok!' );
}

//задание 11
const number = +prompt('Введите число между 0 и 3', '')

switch (number) {
  case 0: 
    alert('Вы ввели число 0');
    break;

  case 1:
    alert('Вы ввели число 1');
    break;

  case 2:
  case 3:
    alert('Вы ввели число 2, а может и 3');
}

//задание 12
function checkAge(age) {
  return (age > 18) || confirm('Родители разрешили?');
 }

function checkAge2(age) {
  return (age > 18) ? true : confirm('Родители разрешили?');
}

//задание 13
function min(a,b) {
  return a < b ? a : b;
}

//задание14
function pow(x, n) {
  let result = x;

  for (let i = 1; i < n; i++){
    result *= x;
  }
  return result;
}

let x = prompt('введите число', '');
let n = prompt('введите степень', '');

if (n >= 1 && n % 1 == 0) {
  alert( pow(x, n) );
} else {
  alert(`степень ${n} должна быть целым положительным числом`);
}

//проходил блок качество кода