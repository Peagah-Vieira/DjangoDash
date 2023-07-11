document.addEventListener('DOMContentLoaded', () => {
    let form_confirm = document.querySelector('#form_confirm_delete_modal')
    let buttons = document.querySelectorAll("[data-target='#leadDeleteModal']");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            if (button.dataset.url) {
                form_confirm.action = button.dataset.url;
            }
        })
    });
    let confirmModal = document.getElementById("confirmDeleteButtonModal")
    confirmModal.addEventListener('click', () => {
        form_confirm.submit();
    });
});