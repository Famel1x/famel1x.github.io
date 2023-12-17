const body = document.querySelector("body");
const btn = document.querySelector("#btn");
const root = document.querySelector(":root");

const themes = {
    default: {
        "--color-primary": "#7380ec",
        "--color-danger": "#ff7782",
        "--color-success": "#41f1b6",
        "--color-warning": "I#ffbb55",
        "--color-white": "#fff",
        "--color-info-dark": "#7d8da1",
        "--color-info-light": "#dce1eb",
        "--color-dark": "#363949",
        "--color-light": "rgba(132, 139, 200, 0.18)",
        "--color-primary-variant": "#111e88",
        "--color-dark-variant": "#677483",
        "--color-background": "#f6f6f9",
    },
    dark:{
        "--color-background": "#181a1e",
        "--color-white": "#202528",
        "--color-dark": "#edeffd",
        "--color-dark-variant": "#a3bdcc",
        "--file-btn-color": "#a3bdcc",
        "--color-light": "rgba(0, 0, 0, 0.4)",
    }
};



// Проверяем наличие переменной в local storage
if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", false);
}

// Считываем данные с local storage
let isDarkTheme = JSON.parse(localStorage.getItem("theme"));

// Устанавливаем текущую тему
changeTheme(isDarkTheme);

btn.addEventListener("click", btnHandler);

// Функция для обработки нажатия кнопки
function btnHandler(e) {
    e.preventDefault;
    isDarkTheme = !isDarkTheme;
    localStorage.setItem("theme", isDarkTheme);
    changeTheme(isDarkTheme);
}
  
// Функция для смены темы
function changeTheme(isDarkTheme) {
    const theme = isDarkTheme ? "dark" : "default";
    Object.entries(themes[theme]).forEach(([key, value]) => {
      root.style.setProperty(key, value);
    });
  }