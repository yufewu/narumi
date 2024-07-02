from . import function

def read_t1t2_report(dir_report):
    with open(dir_report, 'r') as f:
        report_lines = f.readlines()

    reports = []
    for i in range(len(report_lines)):
        if report_lines[i].startswith('Point'): 
            j = i+2
            peak = [[],[]]
            while(report_lines[j] != '\n'):
                line = report_lines[j].split()
                peak[0].append(topspin_to_normal(line[1]))
                peak[1].append(float(line[2]))
                j = j+1
            reports.append(peak)
    
    return reports


def topspin_to_normal(value):
    if value.endswith('u'):
        return float(value[:-2])*1e-6
    elif value.endswith('m'):
        return float(value[:-2])*1e-3
    elif value.endswith('s'):
        return float(value[:-2])
    else:
        return float(value)


class T1t2Report:

    def __init__(self, vdlist, values):
        T1t2Report.vdlist = vdlist
        T1t2Report.values = values

    def fit(self):
        from scipy.optimize import curve_fit
        popt, pconv = curve_fit(function.expdec, self.vdlist, self.values, p0=[0,1,1/self.vdlist[-3]])
        T1t2Report.popt = popt
        return popt
    
    def plotscatter(self):
        import matplotlib.pyplot as plt
        import numpy as np

        # plot
        time_axis = np.linspace(0,self.vdlist[-1],100)

        fig, ax = plt.subplots(figsize=(8,4), constrained_layout=True)
        ax.scatter(self.vdlist, self.values)
        ax.set_xlabel('time (s)')
        ax.set_ylabel('intensity/integral')
        ax.set_xlim(left=0)
        plt.show()

    def plotfit(self):
        import matplotlib.pyplot as plt
        import numpy as np

        # plot
        time_axis = np.linspace(0,self.vdlist[-1],100)

        fig, ax = plt.subplots(figsize=(8,4), constrained_layout=True)
        ax.scatter(self.vdlist, self.values)
        ax.plot(time_axis, function.expdec(time_axis, self.popt[0], self.popt[1], self.popt[2]))
        ax.set_xlabel('time (s)')
        ax.set_ylabel('intensity/integral')
        ax.set_xlim(left=0)
        ax.text(0.75*max(self.vdlist),0.3*max(self.values)+0.7*min(self.values),'T2 = {:.2f} ms'.format(1000/self.popt[2]))
        plt.show()


def main():
    import os
    from dotenv import load_dotenv

    # define data location
    PREFIX = 
    LIB = 
    EXPNAME = 
    EXPNO = 
    procno = 


    dir_exp = os.path.join(PREFIX, LIB, EXPNAME)
    dir_report = os.path.join(PREFIX, LIB, EXPNAME, EXPNO, 'pdata',procno,'ct1t2.txt')


    reports = read_t1t2_report(dir_report)

    for report in reports:
        t1t2_report = T1t2Report(report[0],report[1])
        popt = t1t2_report.fit()

        print('t2 = {:.1f} ms'.format(1000/popt[2]))
        #t1t2_report.plotscatter()
        t1t2_report.plotfit()

        

if __name__ == "__main__": 
    main()
    
