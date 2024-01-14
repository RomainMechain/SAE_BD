document.addEventListener('DOMContentLoaded', function() { 
    document.getElementById('valider').addEventListener('click', function() {
        var selectedDate = document.getElementById('select_date').value;
        console.log(selectedDate);
        let params = new URLSearchParams(window.location.search);
        let id_billet = params.get('id_billet') || '';
        console.log(id_billet);
        fetch('/add_billet', {
            method: 'POST',
            body: JSON.stringify({
                id_billet: id_billet,
                date: selectedDate
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.redirect_url;
            }
            else {
                alert(data.message);
            }
        })
    });
});