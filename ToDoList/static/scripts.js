function getCookie(name) {
    // Get the csrf cookie of the web page
    // This needs to be passed whenever a new HTTP request is made using javascript
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function DeleteTask(taskId) {
    // Call the deleteTask endpoint
    // Sets the csrf token as a header
    // On success the page is reloaded so the changes to the task list can be seen
    const csrftoken = getCookie('csrftoken');
    $.ajax(
        {
        url: '/deleteTask/' +taskId,
        headers: {'X-CSRFToken': csrftoken},
        type: 'PUT',
        success: function () {
            location.reload();
        }
    });
}

function CompleteTask(taskId) {
    // Call the completeTask endpoint
    // Sets the csrf token as a header
    // On success the page is reloaded so the changes to the task list can be seen
    const csrftoken = getCookie('csrftoken');
    $.ajax(
        {
            url: '/completeTask/' + taskId,
            headers: {'X-CSRFToken': csrftoken},
            type: 'PUT',
            success: function () {
                location.reload();
            }
        });
}

function RemoveAllData() {
    // Call the eraseTasks endpoint
    // Sets the csrf token as a header
    // On success the page is reloaded so the changes to the task lists can be seen
    const csrftoken = getCookie('csrftoken');
    $.ajax(
        {
        url: '/eraseTasks',
        headers: {'X-CSRFToken': csrftoken},
        type: 'DELETE',
        success: function () {
            location.reload();
        }
    });
}