# Modified RSA
RSA algorithm uses only two prime numbers to generate a public and private key. As an outcome, it remains vulnerable to prime factorization, cycling, and forward search attacks. Until today, RSA has maintained security by doubling the length of a public key whenever it gets cracked. The security of RSA can be easily compromised with the help of quantum computers. Thus, much research has been carried out and papers have been published for strengthening the RSA Algorithm. One of many is the [Modified RSA Encryption Algorithm]([url](https://ieeexplore.ieee.org/abstract/document/6168406)https://ieeexplore.ieee.org/abstract/document/6168406). After studying this paper, I have created two scripts namely rsa.py and modified-rsa.py for generating key-pairs using RSA and Modified RSA Algorithms respectively.


## Usage of RSA Script

**SAMPLE A: Encrypting and Decrypting message “123” using RSA.
**
**Step 01:** Selecting two large distinct random prime numbers i.e. [p=83 and q=89] 

<img width="420" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/bf840fcd-cb39-4846-8d0e-8758d4630327">

  
**Step 02:** Calculating n, n = p * q, n = 83 * 89, [n = 7387] 

<img width="421" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/12049a2e-58cf-442f-98fe-87726e324e20">


**Step 03:** Calculating ϕ(n) = (p-1) * (q-1), ϕ(n) = (83-1) * (89-1), [ϕ(n) = 7216] 

<img width="437" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/bd799517-6b27-4bd1-94f7-9f9a375819f6">


**Step 04:** Selecting “e” in the range of 1 < e < ϕ(n) and gcd (e, ϕ(n)) = 1, [e = 97] 

<img width="412" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/0f38c2a8-570d-466c-983a-64a131b66056">

  
**Step 05:** Calculating “d” in the range of 1 < d <ϕ(n) and [e * d mod ϕ (n) = 1], [d = 5505] 

<img width="427" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/8daba8a0-1afc-4478-bbfd-40c4523d569f">

  
**Step 06:**  Selecting Plaintext “M”, [M = 123] 

<img width="437" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/3b4c6c81-73cb-4b09-a10c-0971cc0046dd">

  
**Step 07:** Encryption, Cipher text; C = Me mod n, C = 12397 mod 7387, [C = 1369] 

<img width="426" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/169cdf00-03a1-456b-903d-97f03cbe03ad">

  
**Step 08:** Decryption, Plaintext; M = Cd mod n, P = 13695505 mod 7387, [P = 123] 
  
<img width="422" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/2f102b39-cc36-452e-940a-3377dee15985">



## Usage of Modified RSA

**TEST: Encrypting / Decrypting Message “98526” using Modified – RSA Algorithm.** 

**Step 01:** Selecting three large distinct random prime numbers i.e. [p=83 and q=89 and r = 97] 

<img width="415" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/6e57a92c-b3d5-464d-9f11-78203f03b8ce">


**Step 02:** Calculating n, n = p * q * r, n = 83 * 89 * 97, [n =716539] 

<img width="423" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/37900d31-f5a7-4c41-a34f-95674bd4a509">


**Step 03:** Calculating z, z = n – 10, z= 716539 – 10, [z = 716529] 

<img width="412" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/f6bd667a-e1f5-4140-9b28-5f0d04f5709f">


**Step 04:** Calculating ϕ(n) = (p-1) * (q-1) * (r-1), ϕ(n) = (83-1) * (89-1) * (r-1), [ϕ(n) = 692736] 

<img width="417" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/a15630f4-1f6a-42de-bbc3-622a43f45b95">


**Step 05:** Selecting “e” in the range of 1 < e < ϕ(n) and gcd (e, ϕ(n)) = 1, [e = 101] 

<img width="422" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/369e4f9a-1ee4-42f3-a4b7-245a64c116b5">


**Step 06:** Calculating “f”, f = (e * 2) + 1, f = (101 * 2) + 1, [f = 203] 

<img width="430" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/00ae4ba4-e7ab-4607-a57f-6104a159eb62">


**Step 07:** Calculating “d” in the range of 1 < d <ϕ(n) and [e * d mod ϕ (n) = 1], [d =150893] 

<img width="429" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/bc48af3b-f57b-473e-ba1a-5b596d031382">


**Step 08:**  Selecting Plaintext “M”, [M = 98526] 

<img width="432" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/809f0562-37ea-4bed-b5c2-e69f413d51ce">


**Step 09:** Encryption, Cipher text; C = M(f-1)/2 mod (z+10), C = 98526(203-1)/2 mod 716539, [C = 637929] 

<img width="423" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/e1b5905a-c984-423d-b4ce-baf7e1452650">


**Step 10:** Decryption, Plaintext; M = Cd mod (z+10), P = 637929150893 mod 716539, [P = 98526] 

<img width="422" alt="image" src="https://github.com/nishanthakur/Modified-RSA/assets/54204886/d1bf1ace-248c-4047-8593-091702c3ac5f">


**Note:**
 In the above samples, we have generated key pairs and used them to encrypt and decrypt messages that are in numeric form. These messages in the numeric form are obtained after performing ASCII to numeric conversion.
