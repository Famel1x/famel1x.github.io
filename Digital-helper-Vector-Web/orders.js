const Orders = [
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    },
    {
        VK_ID: '862168214',
        Request: 'How are u?',
        Answer: 'good'
    }
]

Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
        <td>${order.VK_ID}</td>
        <td>${order.Request}</td>
        <td>${order.Answer}</td>`

    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})