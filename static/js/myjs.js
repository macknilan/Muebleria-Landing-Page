    //<script src="js/init.js"></script>
    //<script>

    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.sidenav');
        var instances = M.Sidenav.init(elems, {
            edge: 'left',
            draggable: true,
            inDuration: 250,
            outDuration: 200,
            onOpenStart: null,
            onOpenEnd: null,
            onCloseStart: null,
            onCloseEnd: null,
            preventScrolling: true
        });
    });

    $('.fcarousel').flickity({
        setGallerySize: false,
        pageDots: false,
        wrapAround: true,
        //cellAlign: 'center',
        imagesLoaded: true,
    });
    //</script>