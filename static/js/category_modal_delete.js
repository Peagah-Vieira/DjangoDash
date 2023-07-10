document.addEventListener('DOMContentLoaded', () => {
    let form_confirm = document.querySelector('#form_confirm_modal')
    let buttons = document.querySelectorAll("[data-target='#categoryDeleteModal']");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            if (button.dataset.url) {
                form_confirm.action = button.dataset.url;
            }
        })
    });
    let confirmModal = document.getElementById("confirmButtonModal")
    confirmModal.addEventListener('click', () => {
        form_confirm.submit();
    });
});