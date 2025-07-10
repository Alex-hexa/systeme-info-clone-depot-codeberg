import { Client, StatusOK } from 'k6/net/grpc';
import { check, sleep } from 'k6';


export const options = {
stages: [
    { duration: '10s', target: 20 },
    { duration: '10s', target: 20 },
    { duration: '20s', target: 0 },
  ],
};

const client = new Client();
client.load(['definitions'], 'interface.proto');

export default () => {
  client.connect('172.17.0.1:50051', { plaintext: true});

  const data_hexa = { name: 'Hexa' };
  const response_hexa = client.invoke('Greeter/SayHello', data_hexa);

  check(response_hexa, {
    'status is OK': (r) => r && r.status === StatusOK,
  });

  console.log(JSON.stringify(response_hexa.message));

  sleep(2);

  const data_gone = { name: 'Gone' };
  const response_gone = client.invoke('Greeter/SayHello', data_gone);

  check(response_gone, {
    'status is OK': (r) => r && r.status === StatusOK,
  });
  console.log(JSON.stringify(response_gone.message));


  client.close();
  sleep(1);
};