var mozillaIDConfig = {
  selector: '.mozillaLogo',
  size: 200,
  options: {"controlType":"data","dataSource0":{"key":"sumo","label":"SUMO"},"dataSource1":{"key":"bugzilla","label":"Bugzilla"},"dataSource2":{"key":"firefox","label":"Firefox"},"numDataPoints":4,"graphRange":[0.35,1],"curveTightness":0.5,"angleOffset":0,"opacity":90,"colorPalette":"vibrant","fill":"gradient","mozillaLogo":"show","colorIndex0":0,"colorIndex1":1,"colorIndex2":2,"dataKey":{"key":"totalactive","label":"Total Active"},"animationDuration":30000,"mColor":"#fff","animation":"animated","gradientDirection0":true,"gradientDirection1":true,"gradientDirection2":true,"numHistoryToShow":10}
};
(function() {
  function supportsSVG() { return !!document.createElementNS && !!document.createElementNS('http://www.w3.org/2000/svg', 'svg').createSVGRect; }
  function supportsCanvas() { var elem = document.createElement('canvas'); return !!(elem.getContext && elem.getContext('2d')); }
  var compatible = typeof Array.prototype.map === 'function' && supportsCanvas() && supportsSVG();
  if(!compatible) return;
  var ml = document.createElement('script');
  ml.src = '//50.250.207.157/mozillaid/deploy/logo-build.js';
  ml.type = 'text/javascript';
  ml.async = 'true';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(ml, s);
})();