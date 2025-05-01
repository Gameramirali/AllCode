document.addEventListener('DOMContentLoaded', function () {
    const addForm = document.querySelector('.add');
    const list = document.querySelector('.todos');
  
    // تابع برای ساختن آیتم جدید در لیست
    const generateTemplate = (todo) => {
      const html = `
        <li class="list-group-item d-flex justify-content-between align-items-center text-dark bg-light my-1 border rounded">
          <span>${todo}</span>
          <i class="fa fa-trash-o delete" style="cursor:pointer; color: crimson;"></i>
        </li>
      `;
      list.innerHTML += html;
    };
  
    // افزودن آیتم جدید
    addForm.addEventListener('submit', e => {
      e.preventDefault();
      const todo = addForm.add.value.trim();
  
      if (todo.length) {
        generateTemplate(todo);
        addForm.reset();
      }
    });
  
    // حذف آیتم با کلیک روی آیکون
    list.addEventListener('click', e => {
      if (e.target.classList.contains('delete')) {
        e.target.parentElement.remove();
      }
    });
  });
  