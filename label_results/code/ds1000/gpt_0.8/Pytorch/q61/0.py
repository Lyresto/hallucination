output = MyNet(input)
softmax = torch.nn.Softmax(dim=1)
output_softmax = softmax(output)
confidence_score, predicted_class = torch.max(output_softmax, 1)
