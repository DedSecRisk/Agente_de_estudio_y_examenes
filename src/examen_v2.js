/**
 * examen_v2.js
 * Motor de EXAMEN v2 — ParetoTutor Visual
 * Comportamiento:
 *   1) Guardado automático en localStorage (clave: ex_<id>_respuestas).
 *   2) Restauración al reabrir (persistencia entre sesiones).
 *   3) Feedback POR PREGUNTA: al responder se marca ✔ correcta / ✘ incorrecta
 *      y se muestra la justificación inmediatamente (sin botón "ver solución").
 *   4) Barra de progreso fija + contador.
 *   5) Resultado final: global + % + mensaje + dominio POR TEMA + temas a repasar.
 *   6) Reintentar (borra guardado con confirmación).
 *   7) Botón "Repasar tema" que salta a la sección de la guía (ancla interna).
 *
 * Se incluye vía la etiqueta script embebida en el HTML generado (modo offline).
 */
(function(){
  var ID = 'EXAMEN_ID';           // clave única por materia (se reemplaza al generar)
  var PREGUNTAS = [];            // [{id,tema,txt,opts:[A,B,C,D],ans:2,justHTML:'...'}]
  var LSC = 'ex_' + ID + '_respuestas';
  var LS_TEMA = 'ex_' + ID + '_progreso_tema';
  var LS_ULT = 'ex_' + ID + '_ultimo_tema';

  function cargar(){try{return JSON.parse(localStorage.getItem(LSC))||{}}catch(e){return{}}}
function guardar(d){try{localStorage.setItem(LSC, JSON.stringify(d))}catch(e){}}
  function cargarGlobal(){try{return JSON.parse(localStorage.getItem(LS_TEMA))||{}}catch(e){return{}}}
  function guardarGlobal(d){try{localStorage.setItem(LS_TEMA, JSON.stringify(d))}catch(e){}}

  function responder(qid, idx){
    var guardadas = cargar();
    guardadas[qid] = idx;
    guardar(guardadas);
    pintarPregunta(qid, idx);
    actualizarBarra();
  }

  function pintarPregunta(qid, idx){
    var cont = document.getElementById('cont-' + qid);
    var opts = cont.querySelectorAll('.opcion');
    var correcta = -1;
    for (var i = 0; i < PREGUNTAS.length; i++) { if (PREGUNTAS[i].id === qid) { correcta = PREGUNTAS[i].ans; break; } }
    var esCorrecta = (idx === correcta);
    for (var j = 0; j < opts.length; j++) {
      opts[j].classList.add('bloqueada');
      if (j === correcta) opts[j].classList.add('correcta');
      else if (j === idx) opts[j].classList.add('incorrecta');
    }
    var fb = document.getElementById('fb-' + qid);
    var etiqueta = '<div class="caja-' + (esCorrecta ? 'verde' : 'roja') + '">' +
      (esCorrecta ? '✅ <b>¡Correcto!</b>' : '❌ <b>Incorrecto.</b> La respuesta correcta es ' + 'ABCD'[correcta] + ')') + '</div>';
    var just = '';
    for (var k = 0; k < PREGUNTAS.length; k++) {
      if (PREGUNTAS[k].id === qid) { just = PREGUNTAS[k].justHTML; break; }
    }
    fb.innerHTML = etiqueta + just;
    fb.style.display = 'block';
    cont.classList.add('respondida', esCorrecta ? 'ok' : 'bad');
  }
function actualizarBarra(){
    var guardadas = cargar();
    var n = Object.keys(guardadas).length;
    document.getElementById('prog').textContent = n;
    var pct = Math.round(n / PREGUNTAS.length * 100);
    document.getElementById('bar-fill').style.width = pct + '%';
    var btn = document.getElementById('btn-resultados');
    if (btn) btn.style.display = (n >= PREGUNTAS.length) ? 'inline-block' : 'none';
  }

  function inicializar(){
    var guardadas = cargar();
    for (var i = 0; i < PREGUNTAS.length; i++) {
      var q = PREGUNTAS[i];
      var radios = document.querySelectorAll('input[name="' + q.id + '"]');
      for (var j = 0; j < radios.length; j++) {
        var r = radios[j];
        r.addEventListener('change', (function(qid){
          return function(ev){ responder(qid, parseInt(ev.target.value, 10)); };
        })(q.id));
        if (guardadas[q.id] !== undefined && parseInt(r.value, 10) === parseInt(guardadas[q.id], 10)) {
          r.checked = true;
        }
      }
      if (guardadas[q.id] !== undefined) { pintarPregunta(q.id, guardadas[q.id]); }
    }
    actualizarBarra();
  }

  function mostrarResultados(){
    var guardadas = cargar();
    var aciertos = 0, total = PREGUNTAS.length;
    var porTema = {};
    for (var i = 0; i < PREGUNTAS.length; i++) {
      var q = PREGUNTAS[i];
      if (!porTema[q.tema]) porTema[q.tema] = {ok:0, tot:0};
      porTema[q.tema].tot++;
      if (guardadas[q.id] !== undefined && parseInt(guardadas[q.id],10) === q.ans) { aciertos++; porTema[q.tema].ok++; }
    }
    var pct = Math.round(aciertos / total * 100);
    document.getElementById('res-global').textContent = pct + '%';
    document.getElementById('res-detalle').textContent = aciertos + ' / ' + total + ' preguntas correctas';
    document.getElementById('res-msg').textContent = (
      pct >= 80 ? '🏆 ¡Excelente! Dominas el tema.' :
      pct >= 60 ? '✅ Buen nivel: repasa lo indicado abajo.' :
      '📚 Necesitas reforzar los temas marcados abajo.'
    );
    var temasRepaso = [];
    var temasHtml = '';
    Object.keys(porTema).forEach(function(t){
      var o = porTema[t];
      var tpct = Math.round(o.ok / o.tot * 100);
      if (tpct < 60) temasRepaso.push(t);
      temasHtml += '<div class="res-tema"><span class="rt-nombre">' + t + '</span>' +
        '<span class="rt-bar"><span class="rt-fill" style="width:' + tpct + '%"></span></span>' +
        '<span class="rt-pct">' + tpct + '%</span></div>';
    });
    // slug exacto del tema (viene en el JSON); fallback a derivación por si acaso
    function slugDe(t){
      for (var i = 0; i < PREGUNTAS.length; i++) {
        if (PREGUNTAS[i].tema === t && PREGUNTAS[i].slug) return PREGUNTAS[i].slug;
      }
      return t.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
    }
    document.getElementById('res-temas').innerHTML = temasHtml;
    var rep = document.getElementById('res-repasar');
    if (temasRepaso.length) {
      rep.style.display = 'block';
      var enlaces = '';
      temasRepaso.forEach(function(t){
        var slug = slugDe(t);
        enlaces += '<a href="#tema-' + slug + '">📖 Repasar ' + t + '</a>&nbsp;&nbsp;';
      });
      rep.innerHTML = '🔴 <b>Temas a repasar (&lt;60%):</b> ' + enlaces;
    } else {
      rep.style.display = 'none';
    }
    var panel = document.getElementById('res-panel');
    panel.style.display = 'block';
    panel.scrollIntoView({behavior:'smooth'});
  }

  function reintentar(){
    if (!confirm('¿Seguro que quieres reiniciar el examen? Se borrará tu progreso guardado.')) return;
    try{ localStorage.removeItem(LSC); }catch(e){}
    document.querySelectorAll('input[type=radio]').forEach(function(r){ r.checked=false; });
    document.querySelectorAll('.opcion.correcta,.opcion.incorrecta,.opcion.bloqueada').forEach(function(o){
      o.classList.remove('correcta'); o.classList.remove('incorrecta'); o.classList.remove('bloqueada');
    });
    document.querySelectorAll('.ex-feedback').forEach(function(f){ f.style.display='none'; });
    document.querySelectorAll('.pregunta.respondida,.pregunta.ok,.pregunta.bad').forEach(function(p){
      p.classList.remove('respondida'); p.classList.remove('ok'); p.classList.remove('bad');
    });
    document.getElementById('res-panel').style.display = 'none';
    actualizarBarra();
    window.scrollTo(0,0);
  }

  document.addEventListener('DOMContentLoaded', inicializar);
  window.examenV2 = { mostrarResultados: mostrarResultados, reintentar: reintentar };
})();