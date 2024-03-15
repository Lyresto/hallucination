output = MyNet(input)
softmax = torch.nn.Softmax(dim=1)
probabilities = softmax(output)
confidence_score = torch.max(probabilities).item()
