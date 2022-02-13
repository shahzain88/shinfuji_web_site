const menu_button = document.querySelector(".menu");
const banner = document.querySelector(".banner");

const on_menu_click = (e) => {
    console.log()
    if ("menu-card" == banner.classList[1]) {
        console.log("menu-card state click")
        banner.classList = "banner"
        menu_button.classList = "menu";

    } else {
        console.log("banner state click")
        banner.classList += " menu-card ";
        menu_button.classList += " menu-clicked ";
    }
}

menu_button.addEventListener("click", (e) => on_menu_click(e));

