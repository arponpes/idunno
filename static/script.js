window.addEventListener('load', function () {
    document.getElementById('demo').onclick = function changeContent() {
        let cardId = document.getElementById('demo').getAttribute('cardId')
        deleteCard(cardId)
    }
    var deleteCard = function (cardId) {
        fetch('/card/' + cardId, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
})