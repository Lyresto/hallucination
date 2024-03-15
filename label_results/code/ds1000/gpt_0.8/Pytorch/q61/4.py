output = MyNet(input)
softmax = torch.nn.Softmax(dim=1)
probs = softmax(output)
confidence_score = probs.max().item()
