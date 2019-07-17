// index.js
// reloadの応用方法
// キャッシュを利用してリロードする方法
function doReloadWithCache() {

    // キャッシュを利用してリロード
    window.location.reload(false);

}

window.addEventListener('load', function () {

    // ページ表示完了した5秒後にリロード
    setTimeout(doReloadWithCache, 5000);

});