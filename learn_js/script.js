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
//задание 15
let user = {};
user.name = 'John';
user.surname = 'Smith';
user.name = 'Pete';
delete user.name;

//задание 16
let schedule = {};

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false

function isEmpty(obj) {
  for(let key in obj) {
    return false;
  }
  return true;
}

//задание 17
let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}
let sum = 0;

for (let salary in salaries){
  sum += salaries[salary];
}

alert(sum);
//задание 18
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

function multiplyNumeric(obj) {
  for (let key in obj){
    if (typeof obj[key] === 'number'){
      obj[key] *= 2;
    }
  }
}

//задание 19
let calculator = {
  sum() {
    return this.a + this.b;
  },
  mul() {
    return this.a * this.b;
  },
  read() {
    this.a = +prompt('Enter first number', 0);
    this.b = +prompt('Enter second number', 0);
  }
}

//задание 20
function Calculator(){
  this.read = function() {
    this.a = +prompt('Enter first number', 0);
    this.b = +prompt('Enter second number', 0);
  }
  this.sum = function() {
    return this.a + this.b;
  }
  this.mul = function() {
    return this.a * this.b;
  }
}

//задание 21
function Accumulator(startingValue){
  this.value = startingValue;
  this.read = function() {
    this.value += +prompt('Enter a number', 0);
  }
}

//задание 22
function readNumber(){
  let number;

  do {
    num = prompt('Enter a number', 0)
  } while (!isFinite(num));
  if (num === null || num === "") return null;
  return +num;
}

//задание 23
function cheackSpam(str){
  let lowerStr = str.toLowerCase();
  
  return lowerStr.includes('viagra') || lowerStr.includes('xxx');
}

//задание 24
function truncate(str, maxlength){
  return (str.lenght > maxlength) ?
    str.slice(0, maxlength - 1) + '...' : str; //один спец. символ
}
//задание 25
function extractCurrencyValue(str){
  return +str.slice(1);
}

//задание 26
let styles = ['Джаз', 'Блюз'];
styles.push('Рок-н-ролл');
styles[Math.floor((styles.lenght -1) / 2)] = 'Классика';
alert(styles.shift());
styles.unshift('Рэп','Регги');

//задание 27
function sumInput(){
  let numbers = [];

  while(true){

    let value = prompt('enter a number: ', 0)

    if (value === '' || value === null || !isFinite(value)) break;

    numbers.push(+value);
  }

  let sum = 0;
  for (let number of numbers) {
    sum += number;
  }
  return numbers
}

//задание 28
function camelize(str){
  return str.split('-').map((word, index) =>
    index == 0? word : word[0].toUpperCase() + word.slice(1)
  ).join('');
}
//задание 29
function filterRange(arr, a, b){
  return arr.filter(value => (value <= a && value <= b));
}
//задание 30
function filterRangeInPlace(arr, a, b) {

  for (let i = 0; i < arr.length; i++) {
    let val = arr[i];

    if (val < a || val > b) {
      arr.splice(i, 1);
      i--;
    }
  }

}
//задание 31 
let arr = [5, 2, 1, -10, 8];
arr.sort((a, b) => b - a);
alert( arr );

//задание 32
function Calculator(){

  this.methods = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
  };

  this.calculate = function(str){
    let arr = str.split(' '),
      a = +arr[0],
      op = arr[1],
      b = +arr[2]

    if (!this.methods[op] || isNaN(a) || isNaN(b)) {
      return NaN;
    }

    return this.methods[op](a, b);
  }

  this.addMethod = function(name, func){
    this.methods[name] = func;
  };

}
//задание 33
let Vasya = { name: "Вася", age: 25 };
let Petya = { name: "Петя", age: 30 };
let Masha = { name: "Маша", age: 28 };

let uusers = [ Vasya, Petya, Masha ];

let names = uusers.map(item => item.name);

//задание 34
let vasya = { name: "Вася", surname: "Пупкин", id: 1 };
let petya = { name: "Петя", surname: "Иванов", id: 2 };
let masha = { name: "Маша", surname: "Петрова", id: 3 };

let users = [ vasya, petya, masha ];

let usersMapped = users.map(user => ({
  fullName : `${user.name} ${user.surname}`,
  id : user.id,
}))
//задание 35 (те же имена)
function sortByAge(users){
  users.sort((a, b) => a.age - b.age);
}