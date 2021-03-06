import torch
import torch.nn as nn

train_data_normalized = list(map(float, range(50)))

train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)


def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L - tw):
        train_seq = input_data[i : i + tw]
        train_label = input_data[i + tw : i + tw + 1]
        inout_seq.append((train_seq, train_label))
    return inout_seq


train_window = 12
train_inout_seq = create_inout_sequences(train_data_normalized, train_window)


class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (
            torch.zeros(1, 1, self.hidden_layer_size),
            torch.zeros(1, 1, self.hidden_layer_size),
        )

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(
            input_seq.view(len(input_seq), 1, -1), self.hidden_cell
        )
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]


def train_model():
    model = LSTM()
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    epochs = 150

    for i in range(epochs):
        for seq, labels in train_inout_seq:
            optimizer.zero_grad()
            model.hidden_cell = (
                torch.zeros(1, 1, model.hidden_layer_size),
                torch.zeros(1, 1, model.hidden_layer_size),
            )

            y_pred = model(seq)

            single_loss = loss_function(y_pred, labels)
            single_loss.backward()
            optimizer.step()

        if i % 25 == 1:
            print(f"epoch: {i:3} loss: {single_loss.item():10.8f}")

    print(f"epoch: {i:3} loss: {single_loss.item():10.10f}")

    test_inputs = train_data_normalized[-train_window:].tolist()
    print(test_inputs)
