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

/*что-то придумываю
программа, которая отебрает сотрудников на работу
*/
let name = prompt('введите ваше имя', '');
let age = prompt('введите ваш возвраст', '');
let experience = prompt('какой у вас опыт работы(лет)', '');
let requiredSalary = prompt('ваша требуемая зарплата', '');

let isSuitable = age >= 18 && experience >=3 && requiredSalary >= 50000;
alert(isSuitable ? 'вы подходите' : 'вы не подходите');
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
    num2 = 20,
    // result;

if (result === null || result === undefined) {
  if (num1 !== null && num1 !== undefined) {
    result = num1;
  } else {
    result = num2;
  }
}
result ??= num1 ?? num2;