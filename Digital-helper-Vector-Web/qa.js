const Orders = [
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        FileName: 'test',
        FileHref: 'https://images.unsplash.com/photo-1554080353-a576cf803bda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8fDA%3D'
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
    {
        Request: 'How are u?',
        Request_keyword: "how, a, u",
        Answer: 'good',
        File: '',
        FileHref: ''
    },
]

// Функция для загрузки данных из JSON файла
function loadJSON(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'data.json', true);
    xobj.onreadystatechange = function () {
      if (xobj.readyState == 4 && xobj.status == "200") {
        callback(JSON.parse(xobj.responseText));
      }
    };
    xobj.send(null);
  }


// Получение ссылки на таблицу
var table = document.getElementById("data-table");

// Загрузка данных из JSON файла
fetch("./bot.json")
  .then(response => response.json())
  .then(data => {
    // Перебор каждого объекта в JSON данных
    data.forEach(item => {
      // Создание новой строки в таблице
      var row = table.insertRow();

      // Вставка значений из JSON в новые ячейки строки
      var responseTypeCell = row.insertCell();
      responseTypeCell.innerHTML = item.response_type;

      var userInputCell = row.insertCell();
      userInputCell.innerHTML = item.user_input.join(", ");

      var botResponseCell = row.insertCell();
      botResponseCell.innerHTML = item.bot_response;

      var requiredWordsCell = row.insertCell();
      requiredWordsCell.innerHTML = item.required_words.join(", ");
    });
  })
  .catch(error => {
    console.log("Ошибка при загрузке данных из JSON файла:", error);
  });