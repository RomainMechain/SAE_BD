document.addEventListener('DOMContentLoaded', function() {
    let select_type = document.getElementById('select_type');
    let params = new URLSearchParams(window.location.search);
    let id_type = params.get('id_type') || '';
    let search_term = params.get('search_term') || '';

    function loadSelection() {
        let type = JSON.parse(localStorage.getItem('id_type')) || 'all';
        document.getElementById('select_type').value = type;
    }

    select_type.addEventListener('change', function() {
        let type = select_type.value;
        let url = window.location.href.split('?')[0] + '?';
        url += 'id_type=' + type + '&' + 'search_term=' + search_term + '&';

        window.location.href = url;

        localStorage.setItem('id_type', JSON.stringify(type));

    });

    document.querySelector('#search_barre').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
          e.preventDefault(); 
          var searchValue = e.target.value;
          let url = window.location.href.split('?')[0] + '?';
          url += 'id_type=' + id_type + '&' + 'search_term=' + searchValue + '&';

          localStorage.setItem('search_term', JSON.stringify(searchValue));

          window.location.href = url;
        }
    });

    window.onload = function() {
        loadSelection();
    };
 });