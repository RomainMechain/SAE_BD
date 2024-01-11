document.addEventListener('DOMContentLoaded', function() {
    let select_type = document.getElementById('select_type');

    function loadSelection() {
        let type = JSON.parse(localStorage.getItem('id_type')) || 'all';
        document.getElementById('select_type').value = type;
    }

    select_type.addEventListener('change', function() {
        let type = select_type.value;
        let url = window.location.href.split('?')[0] + '?';
        url += 'id_type=' + type + '&';
        let search_term = JSON.parse(localStorage.getItem('search_term')) || '';
        if (search_term != '') {
            url += 'search_term=' + search_term + '&';
        }

        window.location.href = url;

        localStorage.setItem('id_type', JSON.stringify(type));

    });

    document.querySelector('#search_barre').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          e.preventDefault(); 
          var searchValue = e.target.value;
          let url = window.location.href;
          if (! url.includes('id_type')) {
            url = url + "?";
          }
          url += 'search_term=' + searchValue + '&';

          localStorage.setItem('search_term', JSON.stringify(searchValue));

          window.location.href = url;
        }
    });

    window.onload = function() {
        loadSelection();
    };

    window.addEventListener('beforeunload', function(e) {
        localStorage.removeItem('search_term');
        localStorage.removeItem('id_type');
    });
 });