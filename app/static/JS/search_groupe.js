document.addEventListener('DOMContentLoaded', function() { 
    let params = new URLSearchParams(window.location.search);
    let search_term = params.get('search_term') || '';
    let favori = params.get('favori') || '';

    document.querySelector('#search_barre').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          e.preventDefault(); 
          var searchValue = e.target.value;
          let url = window.location.href.split('?')[0] + '?';
          url += 'search_term=' + searchValue + '&' + 'favori=' + favori + '&';

          window.location.href = url;
        }
    });

    document.getElementById('favori').addEventListener('click', function() { 
        var favoriCheckbox = document.getElementById('favori').checked;
        let url = window.location.href.split('?')[0] + '?';
        url += 'search_term=' + search_term + '&' + 'favori=' + favoriCheckbox + '&';

        window.location.href = url;
    });

    window.onload = function() {
        if (favori == 'true') {
            document.getElementById('favori').checked = true;
        }
    };


});