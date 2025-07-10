import http from 'k6/http';
import { sleep, check } from 'k6';

// ramp up de 40 secondes pour 10 utilisateurs, 1 plateau de 20 secondes, redescente identique à la ramp up ?

export const options = {
  stages: [
    { duration: '20s', target: 10 },
    { duration: '10s', target: 10 },
    { duration: '20s', target: 0 },
  ],
};

export default function() {
  let res = http.get('https://quickpizza.grafana.com');
  check(res, { "status is 200": (res) => res.status === 200 });
  sleep(5);
}
