using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Summary description for Class1
/// </summary>
public class ServiceResults
{
    public string Name;
    public string Sirname;
    public string ServiceName;
    public int? Cost;

    public ServiceResults()
    {

}
    public ServiceResults(string name, string sirname, string serviceName, int? cost)
    {
        this.Name = name;
        this.Sirname = sirname;
        this.ServiceName = serviceName;
        this.Cost = cost;

    }
}
