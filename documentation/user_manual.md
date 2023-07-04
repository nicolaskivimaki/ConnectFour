## User manual

### Installation

Once you have downloaded the repository using git clone, you can set up the necessary dependencies by entering the repository and running the command

```bash
poetry install
```

After this, you can run the program with the command

```bash
poetry run invoke start
```

Now the game should open on your screen:

<img width="693" alt="Screenshot 2023-07-05 at 2 37 12" src="https://github.com/nicolaskivimaki/tiralabra_K23/assets/86207135/19af6e37-00b8-4c5e-9676-fb2599ef6ad8">



### How to play

On the start screen, you are able to choose the color of your token and opponent difficulty by clicking on the boxes. Red always goes first. Once you have made your choices, click the "Play" button to begin playing:

<img width="694" alt="Screenshot 2023-07-05 at 2 39 38" src="https://github.com/nicolaskivimaki/tiralabra_K23/assets/86207135/eaba50b5-8751-4fb6-af21-d0404ae16d3f">

Once you have reached the game screen, you can drop your token by moving your mouse onto your desired column and clicking on it. The token will appear in the first empty row.

<img width="697" alt="Screenshot 2023-07-05 at 2 42 55" src="https://github.com/nicolaskivimaki/tiralabra_K23/assets/86207135/9e929b7f-c2f1-47ff-a3a3-1b456df6d527">

The game will end and return to the start screen when either player gets a 4-in-a-row or a stalemate is reached.

### Testing

You can find instructions for running tests in the [Testing Document](https://github.com/nicolaskivimaki/tiralabra-K23/blob/main/documentation/testing_document.md).
