/**
 * WebAppAdapter handles the initial web request and renders the main UI template.
 */
function doGet(e) {
  return HtmlService.createTemplateFromFile('src/ui/Index')
    .evaluate()
    .setTitle('Personal Financial Ledger')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/**
 * Include helper for template partials.
 */
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
