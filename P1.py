class Patient:
    """ base class """

    def __init__(self, name):
        """
        :param name: name of this patient
        """
        self.name = name

    def discharge(self):
        """ abstract method to be overridden in derived classes
        :returns the name and type of the patient when called """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 1000
        #because we do not change the individual cost of patient, so not include in the parenthesis

    def discharge(self):
        print("name: " + self.name + " type:EmergencyPatient")


class HospitalizedPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)
        self.ecost = 2000

    def discharge(self):
        print("name: " + self.name + " type:HospitalizedPatient")


class H2:
    def __init__(self):

        self.cost = 0
        self.patients = []

    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
    # we do not need to include print because we already defined the print previously

    def get_total_cost(self):
        for patients in self.patients:
            self.cost += patients.ecost
        return self.cost

HP1 = HospitalizedPatient("A")
HP2 = HospitalizedPatient("B")

EP1 = EmergencyPatient("C")
EP2 = EmergencyPatient("D")
EP3 = EmergencyPatient("E")

YNHH = H2()

YNHH.admit(HP1)
YNHH.admit(HP2)
YNHH.admit(EP1)
YNHH.admit(EP2)
YNHH.admit(EP3)

YNHH.discharge_all()
total_cost = YNHH.get_total_cost()
print (total_cost)








class Node:
    """ base class """
    def __init__(self, name, cost):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, cost)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_utility(self):

        exp_utility = 0
        i =0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i += 1
        return exp_utility

class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost)
        self.utility = utility

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_utility(self):

        return self.utility


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes):
        Node.__init__(self, name, cost)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()

        return outcomes

    def get_expected_utility(self):
        outcomes = dict()
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_utility()

        return outcomes